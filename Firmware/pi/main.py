import asyncio
import serial
import speech_recognition as sr
from realtime_audio import RealtimeAudioClient
from luma.core.interface.serial import spi
from luma.oled.device import ssd1322
from PIL import Image, ImageDraw

WAKE_WORD = "cypher"
SERIAL_PORT = "/dev/ttyUSB0"
BAUD = 115200

oled_serial = spi(device=0, port=0)
oled = ssd1322(oled_serial)

def oled_show(text):
    img = Image.new("RGB", oled.size)
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, fill="white")
    oled.display(img)

esp = serial.Serial(SERIAL_PORT, BAUD, timeout=1)

def send_cmd(cmd):
    esp.write((cmd + "\n").encode())
  
def handle_intent(text):
    t = text.lower()
    if "forward" in t:
        send_cmd("MOVE_FORWARD")
    elif "left" in t:
        send_cmd("TURN_LEFT")
    elif "stop" in t:
        send_cmd("STOP")
    elif "lights" in t:
        send_cmd("LIGHTS_TOGGLE")

r = sr.Recognizer()
mic = sr.Microphone()

def wait_for_wake():
    with mic as source:
        r.adjust_for_ambient_noise(source)

    while True:
        with mic as source:
            audio = r.listen(source)
        try:
            if WAKE_WORD in r.recognize_google(audio).lower():
                return
        except:
            pass

async def main():
    oled_show("Cypher online")

    while True:
        wait_for_wake()
        oled_show("Listening...")

        client = RealtimeAudioClient()
        await client.run()

        oled_show("Ready")

if __name__ == "__main__":
    asyncio.run(main())
