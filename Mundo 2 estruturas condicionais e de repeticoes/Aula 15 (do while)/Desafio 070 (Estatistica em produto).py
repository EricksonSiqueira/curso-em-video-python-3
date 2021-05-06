# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
print("{:=^30}".format('MERCADÃO DO ERISU'))
soma = maisdemil = maisbarato = c = 0
nomemaisbarato = ''
while True:
    nomeprod = str(input("Nome do produto:"))
    preçoprod = -1
    while preçoprod <=0:
        preçoprod = float(input("Preço do produto: R$"))
    soma += preçoprod
    if c == 0 or preçoprod < maisbarato:
        maisbarato = preçoprod
        nomemaisbarato = nomeprod
    if preçoprod >= 1000:
        maisdemil += 1
    c += 1
    print('-='*15)
    opçao = ' '
    while opçao not in 'SNns':
        opçao = str(input("Deseja continuar?[S/N] ")).strip().upper()[0]
    if opçao in 'NAOnao':
        break
    print('-=' * 15)
print("{:=^30}".format('Fim do programa'))
print(f"\nO total da compra foi R${soma:.2f}\nTemos {maisdemil} produtos custando mais de R$1000.\n"
      f"O produto mais barato foi {nomemaisbarato} custando R${maisbarato:.2f}.")
