#!/usr/bin/python3
'''
Author: Ashwani Sharma
Website: zxcv32.com
Email: ashwani@zxcv32.com
Description: This script allows you to make beeping sound from a raspbery pi which is connected with a buzzer that accept either high or low value. You can specify number of beeps, beep duration and delay between two consecutive beeps.
'''

import RPi.GPIO as GPIO
import time, sys, logging, traceback, os.path
from datetime import datetime


try:
    
    #logging.basicConfig(level=logging.DEBUG)
    
    homedir = os.path.expanduser("~")
    filePath = homedir+"/.script-logs/"
    fileName = "beep.log"
    
    if not os.path.exists(filePath):
        os.makedirs(filePath)

    logging.basicConfig(filename=filePath+fileName, level=logging.INFO)
    beepDuration = 0.25
    beepDelay = 0.25
    beeps = 1
    GPIO_Pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_Pin, GPIO.OUT)

    dateTimeNow = datetime.now()
    logging.info('Executed on:' + str(dateTimeNow))
    
    if len(sys.argv) > 4:
            print("Error: Max number of args is 3.\n\nUsage: beep.py [Arg1 Arg2 Arg3]\n\tArg1: Beep count, Default: 1.\n\tArg2: Beep duration in milliseconds. Default: 250 milliseconds.\n\tArg3: Delay between in milliseconds two consecutive beeps. Default: 250 milliseconds.\n")
            logging.error('Too many command line arguments')
            raise ValueError('ArgumentSizeError')
            
    try:
        if len(sys.argv) > 1:
            beeps = int(sys.argv[1])
            if len(sys.argv) > 2:
                beepDuration = int(sys.argv[2])/1000
                if len(sys.argv) > 3:
                    beepDelay = int(sys.argv[3])/1000
    except:
        raise ValueError('InvalidDataType')
           
    for x in range(0, beeps):
        GPIO.output(GPIO_Pin, GPIO.HIGH)
        time.sleep(beepDuration)
        GPIO.output(GPIO_Pin, GPIO.LOW)
        time.sleep(beepDelay)

    GPIO.output(GPIO_Pin, GPIO.LOW)
    GPIO.cleanup()

except ValueError as err:
    GPIO.cleanup()
    err_msg = err.args[0]   
    if err_msg is 'ArgumentSizeError':
        logging.error('The number of arguments entered were greater than 2')
    elif err_msg is 'InvalidDataType':
        logging.error('only integers allowed in command line inputs')

