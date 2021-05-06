# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
maior = 0
menor = 0
anoatual = datetime.date.today().year
for c in range(0, 7):
    idade = int(input(f"Digite a idade da {c+1}° pessoa: "))
    idade = anoatual - idade
    if idade < 18:
        menor += 1
    elif idade >= 18:
        maior += 1
print(f"{menor} pessoas são menores de idade.\n{maior} pessoas são maiores de idade.")
