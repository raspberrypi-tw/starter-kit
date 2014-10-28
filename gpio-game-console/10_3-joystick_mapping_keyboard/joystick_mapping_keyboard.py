#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2014, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# joystick_mapping_keyboard.py
# Mapping keyboard Up/Down/Right/Left by joystick 
#
# Author : sosorry
# Date   : 08/14/2014
# Origin : https://github.com/tuomasjjrasanen/python-uinput/blob/master/examples/keyboard.py

import uinput
import time
import RPi.GPIO as GPIO
import spidev
import os

GPIO.setmode(GPIO.BOARD)
events = (uinput.KEY_DOWN, uinput.KEY_UP, uinput.KEY_LEFT, uinput.KEY_RIGHT)
device = uinput.Device(events)

spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
    adc = spi.xfer2([1, (8+channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

vrx_channel = 1 
vry_channel = 2 

try:
    while True:
        vrx_pos = ReadChannel(vrx_channel)
        vry_pos = ReadChannel(vry_channel)

        if vry_pos > 700 :
            #print("LEFT")
            device.emit(uinput.KEY_LEFT,  1) 
            time.sleep(0.1)
        elif vry_pos < 100 :
            #print("RIGHT")
            device.emit(uinput.KEY_RIGHT, 1) 
            time.sleep(0.1)
        else :
            device.emit(uinput.KEY_RIGHT, 0) 
            device.emit(uinput.KEY_LEFT,  0) 
            time.sleep(0.1)

        if vrx_pos > 700 :
            #print("DOWN")
            device.emit(uinput.KEY_DOWN, 1) 
            time.sleep(0.1)
        elif vrx_pos < 100 :
            #print("UP")
            device.emit(uinput.KEY_UP,   1) 
            time.sleep(0.1)
        else :
            device.emit(uinput.KEY_UP,   0) 
            device.emit(uinput.KEY_DOWN, 0) 
            time.sleep(0.1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          

