import asyncio
import base64
import json
import sounddevice as sd
import numpy as np
import websockets
import os

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

SAMPLE_RATE = 24000
CHUNK = 1024

class RealtimeAudioClient:
    def __init__(self):
        self.ws = None

    async def connect(self):
        self.ws = await websockets.connect(
            "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview",
            extra_headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "OpenAI-Beta": "realtime=v1"
            }
        )

        await self.ws.send(json.dumps({
            "type": "session.update",
            "session": {
                "modalities": ["text", "audio"],
                "instructions": "You are Cypher, a helpful robotic assistant.",
                "voice": "alloy",
                "audio_format": "pcm16"
            }
        }))

    async def send_audio(self, audio_bytes):
        await self.ws.send(json.dumps({
            "type": "input_audio_buffer.append",
            "audio": base64.b64encode(audio_bytes).decode()
        }))

    async def finalize_audio(self):
        await self.ws.send(json.dumps({"type": "input_audio_buffer.commit"}))
        await self.ws.send(json.dumps({"type": "response.create"}))

    async def receive_audio(self):
        while True:
            msg = json.loads(await self.ws.recv())
            if msg["type"] == "response.audio.delta":
                yield base64.b64decode(msg["delta"])

    async def run(self):
        await self.connect()

        def mic_callback(indata, frames, time, status):
            audio = indata.copy().tobytes()
            asyncio.run_coroutine_threadsafe(
                self.send_audio(audio), asyncio.get_event_loop()
            )

        stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16",
            callback=mic_callback
        )

        with stream:
            await asyncio.sleep(3)
            await self.finalize_audio()

            async for chunk in self.receive_audio():
                samples = np.frombuffer(chunk, dtype=np.int16)
                sd.play(samples, SAMPLE_RATE)
                sd.wait()
