# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
co = {'li': '\033[m',
      'vd': '\033[32m',
      'vm': '\033[31m',
      'az': '\033[34m'}

n1 =int(input(f"{co['az']}Digite um número{co['li']}: "))
n2 =int(input(f"{co['az']}Digite um número{co['li']}: "))
n3 =int(input(f"{co['az']}Digite um número{co['li']}: "))

menor = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
print(f"{co['vm']}{menor}{co['li']} é o{co['vm']} menor valor{co['li']}.")

maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
print(f"{co['vd']}{maior}{co['li']} é o{co['vd']} maior valor{co['li']}.")
