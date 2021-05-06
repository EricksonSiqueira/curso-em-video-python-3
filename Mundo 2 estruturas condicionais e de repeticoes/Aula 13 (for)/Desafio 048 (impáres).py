# Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
v = 0
for c in range(0, 501, 3):
    if c > 0:
        if c%2 != 0:
            v += 1
            s += c
print(f"A soma dos {v} valores é {s}")
