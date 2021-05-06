dia = input('Qual dia você nasceu?')
mes = input('Qual mes você nasceu?')
ano = input('Qual ano você nasceu?')

cores = {'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'azul': '\033[34m',
          'limpar': '\033[m'}

print(f"Você nasceu na data {cores['amarelo']}{dia}{cores['limpar']}/{cores['vermelho']}"
      f"{mes}{cores['limpar']}/{cores['azul']}{ano}{cores['limpar']}")
