# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# ➔ ➝
n1 = int(input("Digite um número inteiro e calcularemos o seu fatorial: "))
fat = n1
print(f"{n1}! = ", end='')
while n1 != 1:
    if n1 != 2:
        print(f"{n1} x ", end='')
    else:
        print(f"{n1} x {n1-1} ", end='')
    fat = fat * (n1-1)
    n1 -= 1
print(f"➔ {fat}")

