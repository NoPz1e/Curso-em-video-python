## Desafio 20
'''
Faça um programa em python
que abra e reproduza o 
áudio de um arquivo MP3.
'''

# importa o pygame
import pygame
pygame.init()

som = pygame.__loader__('ex21.mp3')
som.play()