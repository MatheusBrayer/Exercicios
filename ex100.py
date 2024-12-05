# FUNÇÃO PARA SORTEAR E SOMAR
from random import randint
def sortear():
    print(f'Sorteando 5 valores da lista:',end=' ')
    for num in range(0,5):
        lista.append(randint(0,5))
    for num in lista:
        print(num, end=' ')
    print('PRONTO!')


def soma(lista):
    total=0
    for num in lista:
        if num%2!=0:
            pass
        else:
            total+=num
    print(f'Somando os valores pares de {lista}, o total é {total}.')

lista=[]
sortear()
soma(lista)
lista.clear()
sortear()
soma(lista)