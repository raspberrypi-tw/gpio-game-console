#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# photoresistor.py
# Sense the light by photoresistor
#
# Author : RaspberryPi-spy.co.uk
# Date   : 06/22/2014
# Origin : http://www.raspberrypi-spy.co.uk/2013/10/analogue-sensors-on-the-raspberry-pi-using-an-mcp3008/

import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1800000

def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts,places)
    return volts

light_channel = 0
delay = 1

try:
    while True:
        light_level = ReadChannel(light_channel)
        light_volts = ConvertVolts(light_level, 2)

        print("--------------------------------------------")
        print("Light: {} ({}V)".format(light_level,light_volts))
        #resistor_ohms = int(light_volts/(3.3 - light_volts) * 1000)
        #print("Light: {} ({}V), Resistor: {}(ohms)".format(light_level,light_volts, resistor_ohms))

        time.sleep(delay)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

