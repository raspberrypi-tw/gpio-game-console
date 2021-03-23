#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2021, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# adjust_led_bright.py
# Adjust the bright of a led by software PWM
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO
import time

try:
    input = raw_input
except NameError:
    pass

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

pwm_led = GPIO.PWM(LED_PIN, 100)
pwm_led.start(0)

try:
    while True:
        duty_s = input("Enter Brightness (0 to 100):")
        duty = int(duty_s)

        if duty >= 0 and duty <= 100 :
            pwm_led.ChangeDutyCycle(duty)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    pwm_led.stop()
    GPIO.cleanup()          
