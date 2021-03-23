#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# hc_sr04_measure_distance.py
# Measure the distance between HC-SR04 and nearest wall or solid object.
#
# Author : sosorry
# Date   : 09/13/2014

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
TRIGGER_PIN = 16
ECHO_PIN    = 18
GPIO.setup(TRIGGER_PIN,  GPIO.OUT)
GPIO.setup(ECHO_PIN,     GPIO.IN)
GPIO.output(TRIGGER_PIN, GPIO.LOW)
v = 343		# (331 + 0.6*20)

def measure() :
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)	# 10uS 
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    pulse_start = None
    pulse_end   = None

    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()

    t = pulse_end - pulse_start

    d = t * v
    d = d/2

    return d*100


def measure_average() :
    d1 = measure()
    time.sleep(0.05)
    d2 = measure()
    time.sleep(0.05)
    d3 = measure()
    distance = (d1 + d2 + d3) / 3
	
    return distance

try :
    while True:
        distance = measure_average()
        print("Distance: %.1f (cm)" % distance)
        time.sleep(1)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
