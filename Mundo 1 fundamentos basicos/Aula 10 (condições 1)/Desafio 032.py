# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
co = {'li': '\033[m',
      'vd': '\033[32m',
      'vm': '\033[31m'}

ano = int(input('Digite o ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano{co['vd']} {ano}{co['li']} é {co['vd']}bissexto{co['li']}")
else:
    print(f"O ano{co['vm']} {ano}{co['li']} não é{co['vm']} bissexto{co['li']}!")
