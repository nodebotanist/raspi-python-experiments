import Adafruit_GPIO.Platform as Platform

platform = Platform.platform_detect()

print("Diagnostics:\n")
print("Platform is RPi: {0}", platform == 1)