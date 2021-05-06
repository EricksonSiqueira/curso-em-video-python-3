a = input('Digite algo: ')

co = {'l': '\033[m',
      'vm': '\033[31m',
      'vd': '\033[32m',
      'am': '\033[33m',
      'az': '\033[34m',
      'r': '\033[35m',
      'ca': '\033[36m',
      'cn': '\033[7:37:0m'}

print(f"{co['vm']}Só tem espaços?{co['l']}{co['vd']} {a.isspace()}{co['l']}")
print(f"{co['am']}É numérico?{co['l']}{co['az']} {a.isnumeric()}{co['l']}")
print(f"{co['vm']}É alfabético?{co['l']} {co['am']}{a.isalpha()}{co['l']}")
print(f"{co['az']}É alfabético e numérico?{co['l']} {co['am']}{a.isalnum()}{co['l']}")
print(f"{co['r']}Está todo em maiúsculo?{co['l']}{co['ca']} {a.isupper()}{co['l']}")
print(f"{co['cn']}Está todo em minúsculo?{co['l']}{co['vm']} {a.islower()}{co['l']}")
