# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
import pygame

pygame.mixer.init()

co = {'li': '\033[m', 'vm': '\033[31m', 'vd': '\033[32m'}

r = randint(1, 5)
n1 = int(input('Digite um número inteiro: '))
print(r)

if n1 == r:
    print(f"{co['vd']}Parabéns! Você é muito sortudo!{co['li']}")
    pygame.mixer.music.load('acertou.mp3')
    pygame.mixer.music.play()
    while(pygame.mixer.music.get_busy()):pass
else:
    print(f"{co['vm']}Vishhhhhh! Hoje não é seu dia de sorte!{co['li']}")
    pygame.mixer.music.load('errou.mp3')
    pygame.mixer.music.play()
    while(pygame.mixer.music.get_busy()):pass
