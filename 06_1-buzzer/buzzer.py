#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# buzzer.py
# Make the buzzer to sound with interactive way
#
# Author : Raspberry Pi Cook Book

import RPi.GPIO as GPIO
import time

buzzer_pin = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzzer_pin, GPIO.OUT)

def buzz(pitch, duration) :
    period = 1.0 / pitch
    half_period = period / 2
    cycles = int(duration * pitch)
    for i in xrange(cycles) :
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(half_period)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(half_period)

try:
    while True :
        pitch_s = raw_input("Enter Pitch (200 to 2000): ")
        duration_s = raw_input("Enter Duration (seconde): ")
        buzz(float(pitch_s), float(duration_s))

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
