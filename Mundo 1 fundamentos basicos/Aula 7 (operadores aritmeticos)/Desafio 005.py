#Faça um programa que leia um número inteiro e mostre o seu sucessor e o seu antecessor.

co = {'l': '\033[m', 'vm': '\033[31m',
      'az': '\033[34m',
      'vd': '\033[32m',
      'ro': '\033[35m',
      'am': '\033[33m'}

n1 = int(input(f"{co['az']}Digite um número:{co['l']} "))

ant = n1-1
suc = n1+1

print(f"{co['ro']}{ant}{co['l']} é o seu {co['vm']}antecessor{co['l']}. E{co['am']} {suc} {co['l']}é o seu {co['vd']}sucessor{co['l']}.")
