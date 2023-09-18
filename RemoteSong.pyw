import pygame
import numpy as np
pygame.init()
#Defineste frecventa fiecarei note
C4=161.63
D4=193.66
E4=229.63
F4=249.23
G4=292.00
A4=340.00
B4=393.88
#Defineste durata fiecarei note
QUARTER_NOTE=500
#Creaza o lista cu note si durata lor
melody=[(C4,QUARTER_NOTE),(D4,QUARTER_NOTE),(G4,QUARTER_NOTE),(A4,QUARTER_NOTE),(B4,QUARTER_NOTE),(C4,QUARTER_NOTE*2)]
#Pune piesa in miscare
for note,duration in melody:
    sine_wave=(np.sin(2*np.pi*np.arange(44100*duration/500)*note/44100)).astype(np.float32)
    pygame.mixer.Sound(sine_wave).play()
    pygame.time.wait(duration)
#Iesi din joc
pygame.quit()