#!/usr/bin/python3
#
# evdev_keyboard.py
# Injecting input events. Display "hello" on the console
#
# http://python-evdev.readthedocs.org/en/latest/tutorial.html

import time
from evdev import UInput, ecodes as e

ui = UInput()
# accepts only KEY_* events by default
ui.write(e.EV_KEY, e.KEY_H, 1)  # KEY_H down
ui.write(e.EV_KEY, e.KEY_H, 0)  # KEY_H up
time.sleep(0.1)
ui.write(e.EV_KEY, e.KEY_E, 1)  
ui.write(e.EV_KEY, e.KEY_E, 0)  
time.sleep(0.1)
ui.write(e.EV_KEY, e.KEY_L, 1) 
ui.write(e.EV_KEY, e.KEY_L, 0)
time.sleep(0.1)
ui.write(e.EV_KEY, e.KEY_L, 1)
ui.write(e.EV_KEY, e.KEY_L, 0) 
time.sleep(0.1)
ui.write(e.EV_KEY, e.KEY_O, 1)  
ui.write(e.EV_KEY, e.KEY_O, 0) 
time.sleep(0.1)
ui.syn()
ui.close()


