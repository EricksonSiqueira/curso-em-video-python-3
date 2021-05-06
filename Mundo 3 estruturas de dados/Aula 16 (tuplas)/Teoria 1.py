lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita'
# Tuplas são imutáveis
print(lanche[1])
#lanche[1] = 'Refrigerante'
print(lanche[1])

for pos, c in enumerate(lanche):
    print(f"Eu vou comer {c} na posição {pos}")

print("Rapaz!Tô cheio!")

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print(len(lanche))

print(sorted(lanche))