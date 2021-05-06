# Desenvolva um programa que leia o primeiro termo e a razão de uma
# PA. No final, mostre os 10 primeiros termos dessa progressão.
print('='*20 + '\n10 termos de uma PA\n' + '='*20)

t1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
for c in range(1, 11):
    pa = t1 + (c-1)*r
    print(f"Termo[{c}] = {pa}")
