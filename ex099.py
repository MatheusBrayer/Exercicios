# FUNÇÃO QUE DESCOBRE O MAIOR

from random import randint
from time import sleep
def sorteio():
    print('-'*40)
    print('Analisando os valores passados...')
    lista=[]
    for n in range(0,randint(0,10)):
        lista.append(randint(0,10))
    for n in lista:
        print(n, end=' ')
        sleep(.5)
    print(f'Foram informados {len(lista)} valores ao todo.')
    if len(lista)==0:
        print('Lista de valores vazias!')
    else:
        print(f'O maior valor informado foi {max(lista)}.')

sorteio()
sorteio()
sorteio()