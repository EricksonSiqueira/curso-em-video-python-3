# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
from datetime import date
ano = int(input("Digite o ano em que você nasceu: "))
anoatual = date.today().year
idade = (anoatual - ano)
print(f"Idade do competidor = {idade}")
if idade <= 9:
    print("Este competidor é MIRIM!")
elif 9 < idade <= 14:
    print("Este competidor é INFANTIL!")
elif 14 < idade <= 19:
    print("Este competidor é JÚNIOR!")
elif 19 < idade <=25:
    print("Este competidor é SÊNIOR!")
elif idade >= 25:
    print("Este competidor é MASTER!")