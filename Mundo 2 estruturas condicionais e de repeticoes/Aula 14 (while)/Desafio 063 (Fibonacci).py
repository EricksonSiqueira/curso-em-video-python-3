# Escreva um programa que leia um número N inteiro qualquer e mostre
# na tela os N primeiros elementos de uma Sequência de Fibonacci.
n1 = 0
n2 = 1
c = 1
print('-='*15 + '\nSequência de Fibonacci\n' + '-='*15)
r = int(input("Quantos termos deseja ver? "))
while c < r:
    if c == 1:
        print(f"{n1} ➝ {n2} ", end='')
    else:
        print(f" ➝ {n3} ", end='')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    c += 1
print('...')
