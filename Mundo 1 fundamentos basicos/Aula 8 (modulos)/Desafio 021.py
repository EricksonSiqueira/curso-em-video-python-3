import pygame
pygame.mixer.init()
pygame.mixer.music.load('montero.mp3')
pygame.mixer.music.play(0, 0, 3)
while(pygame.mixer.music.get_busy()):pass
