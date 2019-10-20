#!/usr/bin/env python

import RPi.GPIO as GPIO


import sys

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
