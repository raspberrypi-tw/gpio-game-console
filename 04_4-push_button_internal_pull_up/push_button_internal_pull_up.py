#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_internal_pull_up
# Response when push button is pressed with interrupt way, and de-bounces 
# by software. The GPIO input uses the internal pull-up resistor(50k).
#
# Author : sosorry
# Date   : 02/11/2021

import RPi.GPIO as GPIO                 
import time

GPIO.setmode(GPIO.BOARD)                
BTN_PIN = 11
WAIT_TIME = 200
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def mycallback(channel):
    print("Button pressed @", time.ctime())

try:
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)

    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
