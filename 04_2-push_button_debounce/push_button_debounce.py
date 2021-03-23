#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_debounce.py
# Response when push button is pressed with poll way, and de-bounce by 
# software
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
BTN_PIN = 11
WAIT_TIME = 0.2
GPIO.setup(BTN_PIN, GPIO.IN)
previousStatus = None
previousTime = time.time()
currentTime  = None

try:
    while True:
        input = GPIO.input(BTN_PIN)
        currentTime = time.time()
        if input == GPIO.LOW and previousStatus == GPIO.HIGH and (currentTime - previousTime) > WAIT_TIME:
            previousTime = currentTime
            print("Button pressed @", time.ctime())
        previousStatus = input

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
