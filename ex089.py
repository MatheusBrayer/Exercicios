# PROGRAMA BOLETIM
lista=[]
aluno=[]
while True:
    aluno.append(str(input('NOME:')))
    aluno.append(float(input('NOTA 01:')))
    aluno.append(float(input('NOTA 02:')))
    continuar=str(input('Deseja continuar [S/N]?')).upper().strip()[0]
    lista.append(aluno[:])
    aluno.clear()
    if continuar in 'N':
        break
media=[]
for l in lista:
    media.append((l[1]+l[2])/2)
print(media)
print('=-'*30)
print(f'{"n°":<5}{"NOME":<15}{"MÉDIA":<5}')
print('-'*30)
for l in range(len(lista)):
    print(f'{l+1:<5}{lista[l][0]:<15}{media[l]:<5}')
print('=-'*30)
while True:
    notas_aluno=int(input('Deseja ver a nota de qual aluno (999 interrompe)?'))
    if notas_aluno==999:
        break
    print(f'As notas de {lista[notas_aluno-1][0]} são {lista[notas_aluno-1][1]} e {lista[notas_aluno-1][2]}')
    print('=-'*30)
print()
print('FINALIZANDO...')
print('<<<VOLTE SEMPRE!>>>')