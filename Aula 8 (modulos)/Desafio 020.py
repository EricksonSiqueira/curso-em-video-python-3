from random import shuffle
aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do aluno: ')
aluno3 = input('Digite o nome do aluno: ')
aluno4 = input('Digite o nome do aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(alunos)

print(f'A ordem do sorteio é: {alunos}')
