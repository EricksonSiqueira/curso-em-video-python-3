# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
co = {'li': '\033[m',
      'vd': '\033[32m',
      'ro': '\033[35m'}

sal = float(input(f"{co['ro']}Digite o seu salário:{co['li']}{co['vd']}R${co['li']}"))
if sal > 1250.00:
    sal = sal + (sal*10)/100
else:
    sal = sal + (sal*15)/100
print(f"O seu novo salario é:{co['vd']}R${sal:.2f}{co['li']}")
