# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input("Digite o ano em que você nasceu:"))
anoatual = date.today().year
idade = (anoatual-ano)

print(f"Quem nasceu em {ano} tem {idade} anos.")

if idade < 18:
    print("Você ainda esta muito novo para se alistar.")
    falta = 18-idade
    if falta == 1:
        print("Falta 1 ano para você ter que se alistar")
    elif falta > 1:
        print(f"Faltam {falta} anos para você ter que se alistar")
elif idade == 18:
    print("Você precisa se alistar IMEDIATAMENTE!")
elif idade > 18:
    passou = idade - 18
    if passou > 1:
        print(f"Já passaram {passou} anos do seu alistamento!\nCaso você não tenha se alistado pagará uma multa!")
    elif passou == 1:
        print("Já passou 1 ano do seu alistamento!\nCaso você não tenha se alistado pagará uma multa!")

