# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

co = {'li': '\033[m',
      'vd': '\033[32m',
      'vm': '\033[31m',
      'az': '\033[34m',
      'ro': '\033[35m',
      'am': '\033[33m',
      'ca': '\033[36m'}

n = str(input(f"{co['az']}Digite um número{co['li']}: "))
ni = int(n)
u = 0
d = 0
c = 0
m = 0
if 0 < ni < 10000:
    if 0 < ni < 10:
        u = n
    if 10 < ni < 100:
        u = n[1]
        d = n[0]
    if 100 < ni < 1000:
        u = n[2]
        d = n[1]
        c = n[0]
    if 1000 < ni < 10000:
        u = n[3]
        d = n[2]
        c = n[1]
        m = n[0]

    print(f"O número digitado foi {co['ca']}{n}{co['li']}\n"
          f"A {co['am']}unidade{co['li']} é {co['am']}{u}{co['li']}\n"
          f"A {co['ro']}dezena{co['li']} é {co['ro']}{d}{co['li']}\n"
          f"A {co['az']}centena{co['li']} é {co['az']}{c}{co['li']}\n"
          f"O {co['vd']}milhar{co['li']} é {co['vd']}{m}{co['li']} ")
else:
    print(f"O número digitado é {co['vm']}inválido!{co['li']}")
