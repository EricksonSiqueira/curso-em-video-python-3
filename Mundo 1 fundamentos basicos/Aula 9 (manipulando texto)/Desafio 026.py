# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: '))

qa = frase.upper().count('A')
pa = frase.upper().strip().find('A')
ua = frase.upper().strip().rfind('A')

print(f'Quantidade de letras A é: {qa}\nA primeira posição que ela aparece é: {pa+1}\nA ultima posição que ela aparece é: {ua+1}')
