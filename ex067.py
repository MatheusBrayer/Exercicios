# TABUADA 3.0
from time import sleep
numero=int(input('Qual número deseja ver a tabuada: '))

while True:
    for n in range (0,11):
        print(f'{numero} x {n:2} = {numero*n}')
        n+=1
    print('-'*30)
    sleep(1)
    continuar = int(input('Quer ver a tabuada de qual valor? '))
    print('')
    numero = continuar
    if continuar<0:
        break

print('PROGRAMA ENCERRADO! Volte sempre.')