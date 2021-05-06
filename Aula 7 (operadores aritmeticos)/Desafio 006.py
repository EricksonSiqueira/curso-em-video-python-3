#Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.

co = {'li': '\033[m',
      'vm': '\033[31m',
      'vd': '\033[32m',
      'am': '\033[33m',
      'az': '\033[34m',
      'ro': '\033[35m',
      'ca': '\033[36m',
      'cn': '\033[37m'}

n1 = float(input(f"{co['vd']}Digite um número{co['li']}: "))

do = n1*2 #dobrando o número
tri = n1*3 #triplicando o número
raiz = n1**(1/2) #raiz quadrada desse número

print(f"O {co['am']}número digitado{co['li']} foi{co['am']} {n1}{co['li']}.\nO {co['az']}dobro{co['li']} é"
      f"{co['az']} {do}{co['li']}.\nO {co['ro']}triplo{co['li']} é{co['ro']} {tri}{co['li']}.\n"
      f"A{co['vm']} raiz quadrada{co['li']} é{co['vm']} {raiz:.2f}{co['li']}.")
