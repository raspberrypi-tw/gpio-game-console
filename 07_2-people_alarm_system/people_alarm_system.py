#!/usr/bin/python                                                                                                                                                       
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
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
BOUNCE_TIME = 200
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def callback_function(channel):
    print "Motion detected! ", time.strftime("%H:%M:%S")
    blink_led()

def blink_led():
    for i in range(3) :
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=callback_function, bouncetime=BOUNCE_TIME)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()                              

