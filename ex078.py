# PROGRAMA MAIOR E MENOR VALOR DA LISTA
lista=[]
for v in range(0,5):
    lista.append(input(f'Digite um valor para a posição {v}: '))
print(lista)
print('')
print(f'O número de maior valor encontrado foi {max(lista)} na posição', end=' ')
for c, v in enumerate(lista):
    if v==max(lista):
        print(c, end='...')
print(f'\nO numero de menor valor encontrado foi {min(lista)} na posição', end=' ')
for c, v in enumerate(lista):
    if v==min(lista):
        print(c, end='...')