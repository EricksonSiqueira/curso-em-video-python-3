# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual
# é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
tot = 0
maior = 0
nomemaior = ''
mumenor = 0
for c in range(0, 4):
    print('='*6 + ' {}° pessoa '.format(c+1) + '='*6)
    n = str(input(f"Nome: "))
    i = int(input(f"Idade: "))
    s = str(input(f"Sexo[M/F]: "))
    if i > maior and s.upper() == 'M':
        maior = i
        nomemaior = n
    if s.upper().strip() == 'F':
        if i < 20:
            mumenor += 1
    tot += i
media = tot/4

print(f"Media de idade do grupo é {media:.1f}\nO mais velho tem {maior} anos e seu nome é {nomemaior}\n"
      f"Este grupo possui {mumenor} mulheres abaixo de 20 anos")

