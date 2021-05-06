n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
dr = n1%n2
e = n1**n2

print(f'A soma vale {s}.\nA divisão vale {d:.0f}.\nA multiplicação vale {m}',end=' ')
print(f'\nDivisão inteira é {di}.\nO resto é {dr}.\nA potência é {e}')
