# Crie um programa que vai gerar cinco números aleatório
# e colocar em uma tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
numeros = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
menor = maior = 0
print("Números gerados : ", end='')
for c in range(0, 5):
    print(numeros[c], end=' ')
# minha solução
    """if c == 0:
        menor = numeros[c]
        maior = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print(f'\nO menor número é {menor}\nO maior é {maior}')"""

#Solução Guanabara

print(f"\nO menor valor é {min(numeros)}\nO maior é {max(numeros)}")
