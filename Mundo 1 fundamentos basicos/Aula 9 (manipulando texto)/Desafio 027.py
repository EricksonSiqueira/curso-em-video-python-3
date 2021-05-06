# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome: ')).strip()
n = nome.split()
print(f"Primeiro nome: {n[0]}\nUltimo nome: {n[nome.count(' ')]}")
