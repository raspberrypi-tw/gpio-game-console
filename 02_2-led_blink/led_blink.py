#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2019, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# led_blink.py
# Blinking led without warning (Add try/except)
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO 
import time

LED_PIN = 12	
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

class control_GPIO:
    def __enter__(self):
        pass
    def __exit__(self,type, value, trace):
        print("Exception: KeyboardInterrupt")
        GPIO.cleanup()

with control_GPIO():
    while True:
        print("LED is on")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)

        print("LED is off")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)         
