#  Faça um programa que mostre a tabuada de vários números,
#  um de cada vez, para cada valor digitado pelo usuário.
#  O programa será interrompido quando o número solicitado for negativo.
print('-='*7, 'Tabuada', '-='*7)
while True:
    v = int(input("Deseja ver a tuabuada de qual valor? "))
    if v < 0:
        break
    for c in range(1, 11):
        print(f"{v} x {c} = {v*c}")
print('-='*5, 'Programa encerrado.', '-='*5)
