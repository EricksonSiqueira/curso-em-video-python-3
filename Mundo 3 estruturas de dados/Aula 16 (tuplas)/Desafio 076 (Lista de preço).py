# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
tabela = ('Lapis', 1.75,
          'Borracha', 2.00,
          'Caderno', 15.90,
          'Estojo', 10.00,
          'Mochila', 120.00)

for c in range(0, len(tabela), 2):
    print('{:.<30}R${: >7.2f}'.format(tabela[c], tabela[c+1]))
