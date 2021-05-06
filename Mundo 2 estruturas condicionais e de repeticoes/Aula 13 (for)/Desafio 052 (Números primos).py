# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
n = int(input("Digite um número inteiro: "))
div = 0
for c in range(1, n+1):
    if n % c == 0:
        print('{}{}{}'.format('\033[32m', c, '\033[m'), end=' ')
        div += 1
    else:
        print('{}{}{}'.format('\033[31m', c, '\033[m'), end=' ')
if div <= 2:
    print(f"\n{n} foi dividido {div} vezes.\nÉ um número primo.")
else:
    print(f"\n{n} foi dividido {div} vezes.NÃO é um número primo.")
