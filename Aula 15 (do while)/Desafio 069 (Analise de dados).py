# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
maiordeidade = masculino = mulhervinte = 0
while True:
    r = ' '
    while r not in 'SN':
        r = input(str("Deseja cadastrar uma pessoa? [s/n] ")).strip().upper()[0]
    print('-=' * 15)
    if r in 'NAOnao':
        print('-=' * 15)
        break
    idade = -1
    while idade < 0:
        idade = int(input("Informe a idade da pessoa: "))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input("Informe o sexo da pessoa[M/F]: ")).strip().upper()[0]
    if idade > 18:
        maiordeidade += 1
    if sexo in 'Mm':
        masculino += 1
    if sexo in 'Ff' and idade < 20:
        mulhervinte += 1
    print('-='*15)
print(f"{maiordeidade} são maiores de idade.\n{masculino} são do sexo masculino.\n"
      f"{mulhervinte} são mulheres com menos de 20 anos")
