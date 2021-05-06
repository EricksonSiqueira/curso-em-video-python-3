#Crie um programa que leia um número real qualquer e pegue somente a sua parte inteira
from math import trunc
n1 = float(input('Digite um número: '))
n2 = trunc(n1)
print(f'Você digitou o número {n1} a parte inteira desse número é: {n2}')
