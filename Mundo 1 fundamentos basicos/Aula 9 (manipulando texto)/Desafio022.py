# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome: '))
print(f'Nome maiusculo: {nome.upper()}')
print(f'Nome minusculo: {nome.lower()}')
print(f"Quantidade de letras: {len(nome.replace(' ', ''))}")
separado = nome.split()
print(f'Somente o primeiro nome: {separado[0]}')
