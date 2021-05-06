# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
placarjog = 0
print('-='*6, 'PAR OU IMPAR', '-='*6)
while True:
    jogadoresco = ' '
    jogadornum = -2
    while jogadoresco not in 'parimpar':
        jogadoresco = str(input("Escolha impar ou par: ")).strip().lower()
    while jogadornum > 10 or jogadornum < 0:
        jogadornum = int(input("Digite um número de 0 a 10: "))
    maquina = randint(0, 11)
    r = jogadornum + maquina
    print(f"\nVocê escolheu {jogadoresco}.\nVocê jogou {jogadornum} e a maquina jogou {maquina}."
          f"\nA soma deu {r}.")
    print("DEU PAR." if r % 2 == 0 else "DEU IMPÁR.")
    if r % 2 == 0:
        if jogadoresco == 'par':
            placarjog += 1
            print("BOA JOGADOR! VOCÊ GANHOU!")
        else:
            break
    else:
        if jogadoresco == 'impar':
            placarjog += 1
            print("BOA JOGADOR! VOCÊ GANHOU!\n")
        else:
            break
print(f"\nPutz... Infelizmente você perdeu tente jogar outra vez.\nSeu total de vitorias foi {placarjog}.")
print('\n', '-='*9, 'FIM DO JOGO', '-='*9)
