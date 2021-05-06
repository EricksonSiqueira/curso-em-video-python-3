#  Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
#  alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
co = {'li': '\033[m', 'az': '\033[34m', 'vd': '\033[32m'}
print('-='*9 + 'Gerador de PA' + '-='*9)
p1 = int(input("Primeiro termo: "))
r = int(input("Digite a razão: "))
n = 0
op = 10
cont = 0

while op != 0:
    n = n +1
    pa = p1 + r*(n-1)
    if n <= op:
        print("{}{}{} {}➝{} ".format(co['az'], pa, co['li'], co['vd'], co['li']), end='')
    else:
        print("{}PAUSA{}".format(co['az'], co['li']), end='')
        op = int(input("\nQuantos termos você quer mostrar a mais? "))
        cont -= 1
        n -= 1
        if op != 0:
            op = op + n

    cont += 1
print(f"Progressão finalizada com {cont} termos mostrados.")
print('\n' + '-='*12 + 'FIM' + '-='*11)
