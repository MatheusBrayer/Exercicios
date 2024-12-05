import random
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
anulo3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')

lista = [aluno1, aluno2, anulo3,aluno4]

escolhido = random.choice(lista)

print('O aluno escolhido foi {}.'.format(escolhido))