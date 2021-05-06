# Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
n = int(input("Digite um numero para ver a tabuada dele: "))

print('=-'*3 + f'Tabuada de {n}' + '=-'*3)
for c in range(1, 11):
    print(f"{n} x {c} = {c*n}")
print('=-'*9)
