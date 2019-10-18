import pygame
file = "some.mp3"
pygame.init()
pygame.mixer.init()

#Sound doesnt support mp3
#music = pygame.mixer.Sound(file)
#pygame.mixer.Sound.play(music,0,0,30000)

pygame.mixer.music.load(file)
pygame.mixer.music.set_volume(0.0)
channel = pygame.mixer.music.play()

#while pygame.mixer.Sound.get_busy(): 
i = 0
while i < 10000:
 volCalc = min(1.0, i/10000)
 pygame.mixer.music.set_volume(volCalc)
 #pygame.time.Clock().tick(10)
 print(volCalc)
 i += 1
else:
 print("tock")
