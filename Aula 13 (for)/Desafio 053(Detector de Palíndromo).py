#  Crie um programa que leia uma frase qualquer e diga
#  se ela é um palíndromo, desconsiderando os espaços.
pal = str(input("Digite uma frase: ")).strip()
pal1 = pal.lower()
separado = pal1.split()
junto = ''.join(separado)
inverso = ''
inversoc = ''

for i in range(len(pal)-1, -1, -1):
    inversoc += pal[i]

for c in range(len(junto)-1, -1,-1):
    inverso += junto[c]

print("A frase que você digitou foi: {}{}{}".format('\033[35m', pal, '\033[m'))
print("O inverso dela: {}{}{}".format('\033[33m', inversoc, '\033[m'))
if junto == inverso:
    print("{}É um palíndromo!{}".format('\033[32m', '\033[32m'))
else: print("{}Não é um palíndromo.{}".format('\033[31m', '\033[32m'))
