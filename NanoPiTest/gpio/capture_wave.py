'''
Script to capture digital input changes   
'''

import RPi.GPIO as GPIO
import sys
import time 

DI_PIN_NUM = 12      # DI ping number

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DI_PIN_NUM,GPIO.IN)
 
print ("I get status " ,GPIO.input(DI_PIN_NUM))

def high_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')

#GPIO.add_event_detect(DI_PIN_NUM, GPIO.RISING,callback = high_callback)  # add rising edge detection on$


def main_loop():
    while 1:
        # do your stuff...
        if GPIO.input(DI_PIN_NUM):
            print ('I get it')
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        GPIO.cleanup()
        sys.exit(0)    

