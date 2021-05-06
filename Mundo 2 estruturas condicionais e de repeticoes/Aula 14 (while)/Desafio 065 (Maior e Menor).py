# Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
r = 's'
s = 0
media = 0
maior = 0
menor = 0
c = 0

while r != 'n':
    n = int(input("Digite um número: "))
    if c == 0:
        maior = n
        menor = n
        media = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        media += n
    c += 1
    r = str(input("Deseja continuar? [s/n] ")).lower().strip()
media = media/c
print(f"Você digitou {c} números e a média foi {media}.\nO maior valor foi {maior} e o menor foi {menor}.")
