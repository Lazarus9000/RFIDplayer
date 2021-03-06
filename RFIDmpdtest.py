#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
from mpd import MPDClient
import time
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

thisdict = {
  "PawPatrol": "2efkanyOeo0Vzkli3HfcuU",
  "JaJaDingDong": "ppcOKYrNRnGQbWc5qI5A1w"
}

def playsong(id):
  client.stop()
  client.clear()
  #print(id)
  #print(thisdict)
  #if id does not exist, then music playback stops
  if id in thisdict:
    trackid = thisdict[id]
    track = "spotify:track:" + trackid
    print(track)
    client.add(track)
    client.play()

client = MPDClient()               # create client object
client.timeout = 10                # network timeout in seconds (floats allowed), default: None
client.idletimeout = None          # timeout for fetching the result of the idle command is handled seperately, default: None
client.connect("192.168.1.242", 6600)  # connect to localhost:6600
print(client.mpd_version)          # print the MPD version
print(client.find("any", "spillebillen")) # print result of the command "find any house"
client.clear()
client.setvol(20)

playing = True

while playing == True:
	time.sleep(0.1)
	try:
        	id, text = reader.read()
        	#print(id)
        	print(text)
        	playsong(text.strip())
	finally:
        	GPIO.cleanup()
#        	client.close()                     # send the close command
#        	client.disconnect()

        


