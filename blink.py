import time
import Adafruit_GPIO as GPIO

LED_PIN = 18
LED_STATE = True

GPIO.setup(LED_PIN, GPIO.out)

def loop():
  GPIO.output(LED_PIN, LED_STATE)
  LED_STATE = !LED_STATE
  time.sleep(500)

if __name__ == '__main__':
  try:
    while True:
      loop()
  finally:
    GPIO.cleanup()