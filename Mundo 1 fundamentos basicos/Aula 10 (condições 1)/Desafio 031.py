# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
co = {'li': '\033[m',
      'vd': '\033[32m',
      'vm': '\033[31m'}

dis = int(input('Digite a distancia a ser percorrida na viagem: '))

if dis <= 200:
    pre = 0.5*dis
    print(f"O{co['vd']} preço{co['li']} da sua passagem é {co['vd']}R${pre:.2f}{co['li']}")
else:
    pre = 0.45*dis
    print(f"O{co['vm']} preço{co['li']} da sua passagem é {co['vm']}R${pre:.2f}{co['li']}")
