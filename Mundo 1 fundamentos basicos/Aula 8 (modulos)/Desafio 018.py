from math import sin, cos, tan, radians
a = int(input('Digite o angulo: '))
ag = radians(a)
seno = sin(ag)
cosseno = cos(ag)
tangente = tan(ag)

print(f'Seno({a}) = {seno:.2f}\nCosseno({a}) = {cosseno:.2f}\nTangente({a}) = {tangente:.2f}')
