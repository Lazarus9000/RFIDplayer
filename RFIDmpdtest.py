#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
from mpd import MPDClient
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

thisdict = {
  "PawPatrol": "7n70tzvZDfdAL1j9XqsAbH",
  "JaJaDingDong": "ppcOKYrNRnGQbWc5qI5A1w"
}

client = MPDClient()               # create client object
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("192.168.1.242", 6600)  # connect to localhost:6600
print(client.mpd_version)          # print the MPD version
print(client.find("any", "spillebillen")) # print result of the command "find any house"
client.clear()
client.setvol(50)

try:
        id, text = reader.read()
        print(id)
        print(text)
        playsong(text)
finally:
        GPIO.cleanup()
        client.close()                     # send the close command
        client.disconnect()

        
def playsong(id):
  client.stop()
  client.clear()
  string track = "spotify:track:" + id
  print track
  client.add(track)
  client.play()

