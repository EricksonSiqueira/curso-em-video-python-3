# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
co = {'li': '\033[m',
      'az': '\033[34m',
      'ro': '\033[35m',
      'vd': '\033[32m'}
n = int(input(f"{co['vd']}Digite um número{co['li']}: "))
if n%2 == 0:
    print(f"Esse número é {co['az']}par{co['li']}!")
else:
    print(f"Esse número é {co['ro']}ímpar{co['li']}!")
