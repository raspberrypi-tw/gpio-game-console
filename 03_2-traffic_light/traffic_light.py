#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# traffic_light.py
# A traffic light (Red/Yellow/Green) demostration with Python function syntax
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

def TrafficLight(pin, duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        TrafficLight(RED_PIN, 4);
        TrafficLight(YEL_PIN, 2);
        TrafficLight(GRN_PIN, 4);

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
