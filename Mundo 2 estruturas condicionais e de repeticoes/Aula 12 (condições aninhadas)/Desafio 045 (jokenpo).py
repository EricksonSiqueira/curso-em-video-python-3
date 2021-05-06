from random import randint
from time import sleep
op = ['Pedra', 'Papel', 'Tesoura']
r = randint(1, 3)
print('='*12 + " Jokenpô " + '='*12)
escolha = int(input("Opções:\n"
                    "[1]:Pedra\n"
                    "[2]:Papel\n"
                    "[3]:Tesoura\n"))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!")
sleep(1)
print('=-'*20)
if r == escolha:
    print("Vocês escolheram a mesma opção.\nEMPATE!")
elif escolha == 1 and r == 2:
    print(f"Você escolheu {op[escolha-1]}\nA maquina escolheu {op[r-1]}\nMAQUINA GANHOU.")
elif escolha == 1 and r == 3:
    print(f"Você escolheu {op[escolha-1]}\nA maquina escolheu {op[r-1]}\nJOGADOR GANHOU!")
elif escolha == 2 and r == 1:
    print(f"Você escolheu {op[escolha-1]}\nA maquina escolheu {op[r-1]}\nJOGDOR GANHOU!")
elif escolha == 2 and r == 3:
    print(f"Você escolheu {op[escolha-1]}\nA maquina escolheu {op[r-1]}\nMAQUINA GANHOU.")
elif escolha == 3 and r == 1:
    print(f"Você escolheu {op[escolha-1]}\nA maquina escolheu {op[r-1]}\nMAQUINA GANHOU.")
elif escolha == 3 and r == 2:
    print(f"Você escolheu {op[escolha-1]}\nA maquina escolheu {op[r-1]}\nJOGADOR GANHOU!")
print("=-"*20)
