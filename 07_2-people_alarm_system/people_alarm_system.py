#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# people_alarm_system.py
# Sense human and blink LED with PIR(Passive InfraRed Sensor) sensor
#
# Author : sosorry
# Date   : 10/18/2014

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
PIR_PIN = 26
WAIT_TIME = 200
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

def mycallback(channel):
    print("Motion detected @", time.ctime())
    blink_led()

def blink_led():
    for i in range(3) :
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=mycallback, bouncetime=WAIT_TIME)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()                              

