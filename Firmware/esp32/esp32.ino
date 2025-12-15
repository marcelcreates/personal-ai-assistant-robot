#include <FastLED.h>

#define LED_PIN 15
#define NUM_LEDS 16

#define AIN1 26
#define AIN2 25
#define BIN1 33
#define BIN2 32
#define STBY 27

CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(115200);

  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);
  pinMode(STBY, OUTPUT);
  digitalWrite(STBY, HIGH);

  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.clear();
  FastLED.show();
}

void stopMotors() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);
}

void moveForward() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
}

void turnLeft() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "MOVE_FORWARD") moveForward();
    else if (cmd == "TURN_LEFT") turnLeft();
    else if (cmd == "STOP") stopMotors();
    else if (cmd == "LIGHTS_TOGGLE") {
      fill_solid(leds, NUM_LEDS, CRGB::Blue);
      FastLED.show();
    }
  }
}
