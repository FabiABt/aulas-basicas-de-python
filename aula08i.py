#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
import time
pygame.mixer.init()
pygame.mixer.music.load('./Dream_On.mp3') #D:\projeto\aulas-basicas-de-python
pygame.mixer.music.set_volume(90)
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):
    i=1