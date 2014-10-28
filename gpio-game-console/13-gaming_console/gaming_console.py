#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# gaming_console.py
#
# Author : sosorry
# Date   : 10/28/2014

import RPi.GPIO as GPIO
import uinput
import time
import spidev
import os
from time import gmtime, strftime

def callback_function(channel):    
    if channel == JUMP_PIN :
        device.emit(uinput.KEY_X, 1) # Press X key
        time.sleep(0.4)
        device.emit(uinput.KEY_X, 0) # Cancel press X key
        time.sleep(0.3)
    elif channel == FIRE_PIN :
        device.emit(uinput.KEY_Z, 1) # Press Z key
        time.sleep(0.4)
        device.emit(uinput.KEY_Z, 0) # Cancel press Z key
        time.sleep(0.3)
    else :
        pass

def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

GPIO.setmode(GPIO.BOARD)
JUMP_PIN = 12
FIRE_PIN = 11
BOUNCE_TIME = 200 
GPIO.setup(JUMP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(FIRE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

events = (uinput.KEY_DOWN, uinput.KEY_UP, uinput.KEY_LEFT, uinput.KEY_RIGHT, uinput.KEY_X, uinput.KEY_Z, uinput.KEY_ENTER)
device = uinput.Device(events)

spi = spidev.SpiDev()
spi.open(0,0)

swt_channel = 0
vrx_channel = 1 
vry_channel = 2 

try:
    GPIO.add_event_detect(JUMP_PIN, GPIO.FALLING, callback=callback_function, bouncetime=BOUNCE_TIME)
    GPIO.add_event_detect(FIRE_PIN, GPIO.FALLING, callback=callback_function, bouncetime=BOUNCE_TIME)

    while True:
        vrx_pos = ReadChannel(vrx_channel)
        vry_pos = ReadChannel(vry_channel)
        swt_val = ReadChannel(swt_channel)

        # Right/Left
        if vry_pos > 700 :
            device.emit(uinput.KEY_RIGHT, 0) 
            device.emit(uinput.KEY_LEFT, 1) 
        elif vry_pos < 100 :
            device.emit(uinput.KEY_RIGHT, 1) 
            device.emit(uinput.KEY_LEFT, 0) 
        else :
            device.emit(uinput.KEY_RIGHT, 0) 
            device.emit(uinput.KEY_LEFT, 0) 

        # Up/Down
        if vrx_pos > 700 :
            device.emit(uinput.KEY_UP, 0) 
            device.emit(uinput.KEY_DOWN, 1) 
        elif vrx_pos < 100 :
            device.emit(uinput.KEY_UP, 1) 
            device.emit(uinput.KEY_DOWN, 0) 
        else :
            device.emit(uinput.KEY_UP, 0) 
            device.emit(uinput.KEY_DOWN, 0) 

        # Enter
        if swt_val < 100 :
            device.emit(uinput.KEY_ENTER, 1)
        else :
            device.emit(uinput.KEY_ENTER, 0)

        time.sleep(0.2)

except KeyboardInterrupt:
        print "Exception: KeyboardInterrupt"

finally:
        GPIO.cleanup()

