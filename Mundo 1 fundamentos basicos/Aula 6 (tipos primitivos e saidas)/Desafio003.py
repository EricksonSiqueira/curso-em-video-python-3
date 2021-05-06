n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

co = {'l': '\033[m',
      'vm': '\033[31m',
      'vd': '\033[32m',
      'am': '\033[33m',
      'az': '\033[34m',
      'r': '\033[35m',
      'ci': '\033[36m'}

s = n1+n2


print('{}{}{} + {}{}{} = {}{}{}'.format(co['ci'], n1, co['l'], co['az'], n2, co['l'], co['r'], s, co['l']))
