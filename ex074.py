#NUMEROS ALEATÓRIOS EM TUPLA E MENOR E MAIOR VALOR DENTRO DELA.

# MINHA RESOLUÇÃO

'''
from random import randint
num = (randint(0, 10), randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
num_menor=0
num_maior=0
cont=1
for n in num:
    if cont==1:
        num_maior=n
        num_menor=n
    if cont>1:
        if num_maior < n:
            num_maior = n
        if num_menor > n:
            num_menor = n
    cont+=1
print(num)
print(f'O numero menor é {num_menor}.')
print(f'O numero maior é {num_maior}.')
'''

# RESOLUÇÃO DO PROFESSOR

from random import randint
num = (randint(0, 10), randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
for n in num:
    print( n, end=' ')
print(f'\nO numero menor é {min(num)}.')
print(f'O numero maior é {max(num)}.')