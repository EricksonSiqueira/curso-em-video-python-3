# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Ceará-SC', 'Chapecoense', 'Corinthians',
         'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Intenacional', 'Juventude', 'Palmeiras',
         'Bragantino', 'Santos', 'Sport Recife', 'São Paulo')
print("Primeiros 5 colocados:")
for pos, c in enumerate(times):
    if pos < 5:
        print(f"{pos+1}° : {c}")

print("="*20)
print("Últimos 4 colocados:")
for c in range(16, len(times)):
    print(f'{c+1}° : {times[c]}')

print("="*20)
print("Times em ordem alfabética:")
times2 = sorted(times)
for c in range(0, len(times)):
    print(f'{times2[c]}')

print("="*20)
print(f"O time do Chapecoense está na {times.index('Chapecoense')+1}° colocação.")
