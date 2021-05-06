# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
from random import randint
import pygame

pygame.mixer.init()

print('-=' * 8 + 'Jogo da advinhação' + '-=' * 8)
rm = randint(1, 10)
rj = -1
cont = 0
while rj != rm:
    print(rm)
    rj = int(input("Digite um número de 1 à 10 e teste sua sorte: "))
    cont = cont + 1
    if rj != rm:
        pygame.mixer.music.load("errou.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.get_busy(): pass
    if rj > rm:
        print("Menos... Tente outra vez.")
    if rj < rm:
        print("Mais... Tente outra vez.")

if cont == 1:
    print("\nVocê só precisou de 1 tentativa.\nParabéns!! Você está com MUITA sorte hoje.")
elif cont < 4:
    print(f"\nVocê só precisou de {cont} tentativas.\nSua sorte hoje está boa.")
elif cont < 10:
    print(f"\nVocê precisou de {cont} tentativas.\nHoje você não está com muita sorte.")
else:
    print("\nCARAMBA!!! QUE AZAR!!\nVocê precisou de 10 tentativas pra acertar.")
print('-=' * 25)
