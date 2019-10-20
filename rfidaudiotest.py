#!/usr/bin/env python

import RPi.GPIO as GPIO


import sys

from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

import pygame
file = "some.mp3"
pygame.init()
pygame.mixer.init()

#Sound doesnt support mp3
#music = pygame.mixer.Sound(file)
#pygame.mixer.Sound.play(music,0,0,30000)

pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(1.0)

cardread = ''

try:
        id, text = reader.read()
        print(id)
        print(text)
        cardread = text
finally:
        GPIO.cleanup()
        channel = pygame.mixer.music.play()

#while pygame.mixer.Sound.get_busy(): 
i = 0
print("cardread: " + cardread)
while i < 10000:
 if cardread == "1": 
  volCalc = min(1.0, i/10000)
  pygame.mixer.music.set_volume(volCalc)
  #pygame.time.Clock().tick(10)
  print(volCalc)
  
 if cardread == "2":
  print(syke)

 i += 1

else:
 print("tock")     
