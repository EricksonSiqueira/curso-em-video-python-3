# Escrever um programa que leia um número qualquer e transforme ele em
# 1 - Binário
# 2 - octal
# 3 - hexadecimal
n = int(input("Digite um número:"))
r = int(input("Opções:\n"
              "[1]Binário:\n"
              "[2]Octal:\n"
              "[3]Hexadecimal:\n"))
if r == 1:
    print(f"O número {n} em binário é {bin(n)[2:]}")
elif r == 2:
    print(f"O número {n} em octal é {oct(n)[2:]}")
elif r == 3:
    print(f"O número {n} em hexadecimal é {hex(n)[2:]}")
else:
    print("{}Opção inválida, tente novamente.{}".format('\033[31m', '\033[m'))

