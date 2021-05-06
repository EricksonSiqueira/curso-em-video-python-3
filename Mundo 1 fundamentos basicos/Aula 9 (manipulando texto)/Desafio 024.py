# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cid = str(input('Digite o nome da sua cidade: '))
san = cid.split()
print('santo' in san[0].lower())
