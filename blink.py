import time
import RPi.GPIO as GPIO

def loop():
  GPIO.output(LED_PIN, LED_STATE)
  LED_STATE = not LED_STATE
  time.sleep(500)

if __name__ == '__main__':
  try:
    LED_PIN = 18
    LED_STATE = True

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_PIN, GPIO.OUT)
    while True:
      loop()
  finally:
    GPIO.cleanup()