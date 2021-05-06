# Refaça o DESAFIO 035 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

l1 = float(input("Digite o primeiro segmento:"))
l2 = float(input("Digite o segundo segmento:"))
l3 = float(input("Digite o terceiro segmento:"))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos acima PODEM formar um triangulo!")
    if l1 == l2 == l3:
        print("Este triângulo é EQUILÁTERO!")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("Este triângulo é ESCALENO!")
    else:
        print("Este triângulo é ISÓSCELES!")
else:
    print("Esses segmentos NÃO formam um triângulo!")

