#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# tilt_switch.py
# Response when tilt switch is triggered with interrupt way, and 
# de-bounces by software
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO                 
import time

GPIO.setmode(GPIO.BOARD)                
BTN_PIN = 11
WAIT_TIME = 200
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def mycallback(channel):                                                 
    print("Switch tilted @", time.ctime())

try:
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
