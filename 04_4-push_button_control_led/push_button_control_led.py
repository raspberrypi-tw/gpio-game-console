#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_control_led.py
# Turn on the led when push button is pressed with interrupt way, and de-bounces by software
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO                 
import time

GPIO.setmode(GPIO.BOARD)                
BTN_PIN = 11
LED_PIN = 12				
BOUNCE_TIME = 200
status = GPIO.LOW
GPIO.setup(BTN_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT, initial=status) 

def callback_function(channel):                                                 
	print("Button pressed"), time.strftime("%Y-%m-%d %H:%M:%S")
	global status
	if status == GPIO.LOW:
		status = GPIO.HIGH
	else:
		status = GPIO.LOW
	GPIO.output(LED_PIN, status)

try:
	GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=callback_function, bouncetime=BOUNCE_TIME)

	while True:
		time.sleep(10)

except KeyboardInterrupt:
	print "Exception: KeyboardInterrupt"

finally:
	GPIO.cleanup()          
