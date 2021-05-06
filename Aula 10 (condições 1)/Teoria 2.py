n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1+n2)/2

if media >= 7:
    print(f'Parabéns! Você foi aprovado! Sua nota é {media:.2f}')
else:
    print(f'Poxa, você foi reprovado! Sua nota é {media:.2f}')
