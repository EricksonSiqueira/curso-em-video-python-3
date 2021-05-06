# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
co = {'li': '\033[m',
      'vm': '\033[31m',
      'vd': '\033[32m'}

v = int(input('Digite a velocidade atual do carro: '))
if v > 80:
    multa = (v-80)*7
    print(f"{co['vm']}Você foi multado!{co['li']} O valor da multa é{co['vm']} R${multa:.2f}{co['li']}")
else:
    print(f"Você está dentro da velocidade permitida, logo{co['vd']} não será multado{co['li']}.")
