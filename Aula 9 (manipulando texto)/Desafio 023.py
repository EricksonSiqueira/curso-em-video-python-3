# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = str(input('Digite um número: '))

m = numero[0]
c = numero[1]
d = numero[2]
u = numero[3]

print(f'Solução string (com falha)\nMilhar:{m}\nCentena:{c}\nDezena:{d}\nUnidade:{u}\n\n' + '-'*20)

# Solução matematica
num = int(numero)
u = num//1 % 10
d = num//10 %10
c = num//100 % 10
m = num //1000 %10

print(f'Solução matematica:\nMilhar:{m}\nCentena:{c}\nDezena:{d}\nUnidade:{u}')

