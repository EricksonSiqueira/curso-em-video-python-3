# Crie um programa que mostre na tela todos os números
# pares que estão no intervalo entre 1 e 50.
i = 0
print('-='*5 + 'Tabela de pares' + '-='*5)
for c in range(0, 51, 2):
    if c > 0:
        i += 1
        print(f"Par[{i}] = {c}")
print('=-'*15)
