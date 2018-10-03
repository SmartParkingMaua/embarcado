# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:36:33 2018

@author: root
"""

from gpiozero import LED
from time import sleep

led = LED(5)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)