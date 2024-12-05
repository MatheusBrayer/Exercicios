# PROGRAMA MEGA SENHA
from random import randint
from time import sleep
lista=[]
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
vezes_sorteadas=int(input('Quantas vezes quer que eu sorteie? '))
for l in range(0,vezes_sorteadas):
    sleep(.5)
    for l in range(0,6):
        numero_sorteado=(randint(0,100))
        if numero_sorteado not in lista:
            lista.append(numero_sorteado)
    lista.sort()
    print(lista)
    lista.clear()
print('-'*30)
print(F'{"BOA SORTE!":^30}')