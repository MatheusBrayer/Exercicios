# CONTADOR
from time import sleep
from operator import itemgetter
def contador(n1, n2, n3):
    print('-' * 30)
    print(f'Contagem de {n1} até {n2} de {n3} em {n3}')
    for n in range(n1,n2+1, n3):
        print(n, end=' ')
        sleep(.5)
    print('FIM!')


contador(1,10, 1)
print()
contador(10, -1, -2)
print()
print('Agora é a sua vez de personalisar a contagem!')
n1=int(input('Inicio: '))
n2=int(input('Fim: '))
n3=int(input('Passo: '))
if n1>n2 and n3>0:
    n3*=-1
contador(n1,n2,n3)