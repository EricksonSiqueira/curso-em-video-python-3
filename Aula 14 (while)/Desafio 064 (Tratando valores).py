#  Crie um programa que leia vários números inteiros pelo teclado.
#  O programa só vai parar quando o usuário digitar o valor 999, que é a
#  condição de parada. No final, mostre quantos números foram digitados
#  e qual foi a soma entre eles (desconsiderando o flag).
r = c = s = 0
es = '          '
print("=-"*15 + '\n{}SOMADOR{}\n'.format(es, es) + '-='*15)
while r != 999:
    r = int(input("Digite um número[999 para parar]: "))
    if r == 999:
        print(f"Você digitou {c} números e a soma deles é {s}.")
    else:
        s += r
        c += 1