#Crie um programa que leia as 2 notas de um aluno e calculo sua média.

co = {'li': '\033[m',
      'vm': '\033[31m',
      'vd': '\033[32m',
      'am': '\033[33m',
      'az': '\033[34m',
      'ro': '\033[35m'}

n1 = float(input(f"{co['vd']}Digite sua primeira nota{co['li']}: "))
n2 = float(input(f"{co['vd']}Digite sua segunda nota{co['li']}: "))

md = (n1+n2)/2

print(f"Sua{co['az']} média{co['li']} é {co['vm']}{md}{co['li']}.")
