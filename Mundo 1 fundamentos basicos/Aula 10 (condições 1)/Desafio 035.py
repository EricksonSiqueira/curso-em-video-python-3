# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
co = {'li': '\033[m',
      'vd': '\033[32m',
      'vm': '\033[31m',
      'ca': '\033[36m'}

r1 = float(input(f"{co['ca']}Digite o comprimeiro da reta 1{co['li']}:"))
r2 = float(input(f"{co['ca']}Digite o comprimeiro da reta 2{co['li']}:"))
r3 = float(input(f"{co['ca']}Digite o comprimeiro da reta 3{co['li']}:"))
if r1 < r2+r3 and r2 < r1 + r3 and r3 < r1+r2:
    print(f"As retas acima {co['vd']}PODEM{co['li']} formar um triângulo!")
else:
    print(f"As retas acima {co['vm']}NÃO PODEM{co['li']} formar um triângulo!")
