#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# traffic_light_nonstructure.py
# A traffic light (Red/Yellow/Green) demostration
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
RED_PIN = 11    # GPIO17
YEL_PIN = 12    # GPIO18
GRN_PIN = 13    # GPIO27

GPIO.setup(RED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YEL_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GRN_PIN, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(RED_PIN, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(RED_PIN, GPIO.LOW)

        GPIO.output(YEL_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(YEL_PIN, GPIO.LOW)

        GPIO.output(GRN_PIN, GPIO.HIGH)
        time.sleep(4)
        GPIO.output(GRN_PIN, GPIO.LOW)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
