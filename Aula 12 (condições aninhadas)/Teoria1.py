# elif = else if

co = {'li': '\033[m',
      'az': '\033[34m',
      'vd': '\033[32m',
      'vm': '\033[31m'}

nome = str(input("Qual o seu nome?"))
if nome == 'Erickson':
    print(f"Que nome{co['vd']} bonito!{co['li']}")
elif nome == 'Samuel':
    print(f"Que nome {co['vm']}feio!!{co['li']}")
elif nome == 'Anna':
    print("Você tem o nome do amor da minha vida!")
elif nome in 'Claudia Ana Maria':
    print("Seu nome é muito popular no Brasil!")
else:
    print(f"Que nome normal.")
print(f"Prazer em te conhecer,{co['az']} {nome}{co['li']}!!")