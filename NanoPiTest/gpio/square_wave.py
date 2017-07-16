''' 
script to generate a square wave.  
''' 


import RPi.GPIO as GPIO
import time

DO_PIN_NUM = 7      # DO ping number 
interval_sec = 1;   # interval value in second 
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DO_PIN_NUM,GPIO.OUT)
while True:
        GPIO.output(DO_PIN_NUM,True)
        time.sleep(interval_sec)
        GPIO.output(DO_PIN_NUM,False)
        time.sleep(interval_sec)