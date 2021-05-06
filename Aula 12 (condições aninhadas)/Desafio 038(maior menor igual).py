# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
n1 = float(input("Digite um número:"))
n2 = float(input("Digite outro número:"))

if n1 > n2:
    print(f"{n1:.2f} é maior que {n2:.2f}")
elif n1 < n2:
    print(f"{n2:.2f} é maior que o {n1:.2f}")
else:
    print(f"Os valores são iguais!")
