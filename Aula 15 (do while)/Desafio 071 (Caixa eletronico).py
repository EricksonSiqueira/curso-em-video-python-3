#  Crie um programa que simule o funcionamento de um caixa eletrônico.
#  No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
#  o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print("{:=^34}".format(' BANCO DO ERISU '))
valor = float(input("Quando você deseja sacar? R$"))
cinquenta = vinte = dez = um = 0
while True:
    if valor // 50 >= 1:
        cinquenta = valor // 50
        valor = valor % 50
        print(f"Total de {cinquenta:.0f} cedulas de R$50")
    elif valor // 20 >= 1:
        vinte = valor // 20
        print(f"Total de {vinte:.0f} cedulas de R$20")
        valor = valor % 20
    elif valor // 10 >= 1:
        dez = valor // 10
        valor = valor % 10
        print(f"Total de {dez:.0f} cedulas de R$10")
    elif valor // 1 >= 1:
        um = valor // 1
        valor = valor % 1
        print(f"Total de {um:.0f} cedulas de R$1")
    if valor <= 0:
        break
print("="*36)
print("OBRIGADO POR UTILIZAR OS SERVIÇOS DO BANCO ERISU!\nTENHA UM ÓTIMO DIA! VOLTE SEMPRE!")
