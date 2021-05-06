from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hip = hypot(co, ca)
print(f'A hipotenusa é: {hip}.')