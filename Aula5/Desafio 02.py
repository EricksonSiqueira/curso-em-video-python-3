nome = str(input('Qual o seu nome?')).strip()
co = {'l': '\033[m', 'vm': '\033[31m',
      'vd': '\033[32m',
      'am': '\033[33m',
      'az': '\033[34m',
      'r': '\033[35m'}
print(f"{co['vd']}Prazer em te conhecer {co['l']}{co['r']}{nome}{co['l']}{co['am']}!!")
