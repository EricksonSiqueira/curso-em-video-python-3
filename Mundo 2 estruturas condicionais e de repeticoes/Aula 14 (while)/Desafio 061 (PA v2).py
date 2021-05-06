# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
co = {'li': '\033[m', 'az': '\033[34m', 'vd': '\033[32m'}
print('-='*9 + 'Gerador de PA' + '-='*9)
p1 = int(input("Primeiro termo: "))
r = int(input("Digite a razão: "))
cont = 0

while cont != 10:
    cont = cont +1
    pa = p1 + r*(cont-1)
    if cont < 10:
        print("{}{}{} {}➝{} ".format(co['az'], pa, co['li'], co['vd'], co['li']), end='')
    else:
        print("{}{}{}".format(co['az'], pa, co['li']), end='')
print('\n' + '-='*12 + 'FIM' + '-='*11)
