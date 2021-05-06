# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('APRENDER',
            'PROGRAMAR',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')

for c in range(0, len(palavras)):
    print(f"Na palavra {palavras[c]} temos ", end='')
    palavra = palavras[c]
    for i in range(0, len(palavra)):
        if palavra[i] in 'AEIOU':
            print(palavra.lower()[i], end=' ')
    print('\n', end='')

# forma do Guanabara
for p in palavras:
    print(f"\nNa palavra {p} temos ", end='')
    for l in p:
        if l in 'AEIOU':
            print(l.lower(), end=' ')
