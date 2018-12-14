#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
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

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

pwm_led = GPIO.PWM(LED_PIN, 100)
pwm_led.start(0)
duty = 1
addormin = 1

try:
    while True:

        addormin = (duty == 100 and -1) or (duty == 1 and 1) or addormin

        pwm_led.ChangeDutyCycle(duty)

        duty += addormin

        time.sleep(0.01)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    pwm_led.stop()
    GPIO.cleanup()
