# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
menor = 0
maior = 0

for c in range(0, 5):
    p = int(input(f"Digite o peso da {c+1}° pessoa: "))
    if c == 0:
        menor = p
        maior = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p

print(f"O maior peso é {maior}kg.\nO menor peso é {menor}kg.")
