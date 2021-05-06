# Desenvolva um programa que leia quatro
# valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))
           , int(input('Digite um número: ')))
print('='*45)
tres = 0
noves = numeros.count(9)
if numeros.count(3) > 0:
    tres = numeros.index(3)
    print(f'O primeiro valor 3 foi digitado na {tres+1}ª posição.')
else:
    print('O valor 3 não foi digitado,sua posição não existe.', end='')

print(f'\nO valor 9 apareceu {noves} vezes.')
print("Os números pares foram: ", end='')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')
print('\n', '='*45)
