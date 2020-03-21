#!/usr/bin/python3

import os

os.system("vcgencmd measure_temp | egrep -o '[0-9]*\.[0-9]*'")
