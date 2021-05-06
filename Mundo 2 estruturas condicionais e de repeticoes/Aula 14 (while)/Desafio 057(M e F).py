# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
r = ''
while r != 'M' and r != 'F':
    r = str(input('Digite o seu sexo[M/F]: ')).upper()
if r == 'M':
    print("Seu sexo é masculino.")
else:
    print("Seu sexo é feminino.")
