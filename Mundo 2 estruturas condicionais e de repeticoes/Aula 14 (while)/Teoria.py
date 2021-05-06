'''for c in range (1, 10):
    print(c)
print('FIM')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
r = 'S'
while r != 'N':
    n = int(input("Digite um número: "))
    r = str(input("Quer continuar?[S/N] ")).upper()
print('FIM')'''

r = 1
p = i = 0
while r != 0:
    r = int(input("Digite um número: "))
    if r % 2 == 0 and r != 0:
        p += 1
    elif r % 2 != 0 and r != 0:
        i += 1
print(f"Dos números digitados {p} são pares e {i} são ímpares.")
