import time
import RPi.GPIO as GPIO

LED_PIN = 18
LED_STATE = True

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)

def loop():
  global LED_STATE
  GPIO.output(LED_PIN, LED_STATE)
  LED_STATE = not LED_STATE
  time.sleep(500)
  
if __name__ == '__main__':
  try:
    while True:
      loop()
  finally:
    GPIO.cleanup()
