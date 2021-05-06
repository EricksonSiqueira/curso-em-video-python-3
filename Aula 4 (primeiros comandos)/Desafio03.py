n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número para ser somado ao ultimo: '))
n3 = (n1+n2)

c = {'l': '\033[m',
         'v': '\033[32m',
         'am': '\033[33m',
         'r': '\033[35m'}

print(f"A soma de {c['v']}{n1}{c['l']} + {c['am']}{n2}{c['l']} é {c['r']}{n3}{c['l']}")
