#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_poll.py
# Response when push button is clicked with poll way
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO
import time
from time import gmtime, strftime

GPIO.setmode(GPIO.BOARD)
BTN_PIN = 11
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(BTN_PIN) == GPIO.LOW:
            print("Button.Click"), strftime("%Y-%m-%d %H:%M:%S", gmtime())

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
