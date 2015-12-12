#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# pir.py
# Sense human and print message with PIR(Passive InfraRed Sensor) sensor
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 26
BOUNCE_TIME = 200
GPIO.setup(PIR_PIN, GPIO.IN)

def callback_function(channel):
    print "Motion detected! ", time.strftime("%H:%M:%S")

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=callback_function, bouncetime=BOUNCE_TIME)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
