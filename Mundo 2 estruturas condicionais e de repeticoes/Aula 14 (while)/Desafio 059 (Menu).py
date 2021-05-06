# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
op = -1
while op != 5:
    print("-="*7 + 'Opções' + '-='*7)
    op = int(input("[ 1 ] somar\n"
                   "[ 2 ] multiplicar\n"
                   "[ 3 ] maior\n"
                   "[ 4 ] novos números\n"
                   "[ 5 ] sair do programa\n"
                   ":"))
    if op == 1:
        soma = n1 + n2
        print("\n O valor da soma é {}.\n".format(soma))
    elif op == 2:
        multiplicar = n1 * n2
        print("\nO valor da multiplicação é {}.\n".format(multiplicar))
    elif op == 3:
        if n1 > n2:
            maior = n1
            print(f"O maior é {maior}.\n")
        else:
            maior = n2
            print(f"O maior é {maior}\n")
    elif op == 4:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
    if op != 5:
        sleep(2)

print("-="*6 + 'FIM' + '-='*6)
