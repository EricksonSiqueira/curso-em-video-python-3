#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

sal = float(input('Digite o seu salario atual:R$'))

salnovo = sal+(sal*15)/100 #calculando 15% e somando ao salario antigo


print(f'O seu novo salario é: R${salnovo:.2f}')
