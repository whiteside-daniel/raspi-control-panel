import RPi.GPIO as GPIO
import time as time

dp = 7 #set data pin
groundPin = 6 #save groundPin although not used in this code
GPIO.setmode(GPIO.BOARD) #set board mode

GPIO.setup(dp, GPIO.OUT) #set pin mode

GPIO.output(dp, GPIO.HIGH) #set pin high
time.sleep(1)
GPIO.output(dp, GPIO.LOW)
time.sleep(1)
GPIO.output(dp, GPIO.HIGH)
time.sleep(1)
GPIO.output(dp, GPIO.LOW)

print('done')