#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# tilt_switch.py
# Response when tilt switch is triggered with interrupt way, and de-bounces by software
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO                 
import time

GPIO.setmode(GPIO.BOARD)                
BTN_PIN = 11
BOUNCE_TIME = 200
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP, initial=GPIO.HIGH)

def callback_function(channel):                                                 
    print("Tilt.Switch"), time.strftime("%Y-%m-%d %H:%M:%S")

try:
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=callback_function, bouncetime=BOUNCE_TIME)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
