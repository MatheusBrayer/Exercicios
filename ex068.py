# JOGO PAR OU IMPAR
from random import randint
from time import sleep
print('-'*30)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-'*30)
contador=0
while True:
    jogador=int(input('Digite um valor: '))
    opção=str(input('Par ou Impar? ')).upper().strip()[0]
    while opção not in 'PI':
        opção = str(input('Par ou Impar? ')).upper().strip()[0]
    computador=randint (1,10)
    soma=jogador+computador
    print('-'*30)
    if soma%2==0 and opção=='P':
        contador+=1
        print('-' * 30)
        print(f'Você escolheu {jogador} e o computador {computador}. O total deu {soma}, É PAR!')
        print('-' * 30)
    elif soma%2!=0 and opção=='I':
        contador += 1
        print('-' * 30)
        print(f'Você escolheu {jogador} e o computador {computador}. O total deu {soma}, É IMPAR!')
        print('-' * 30)
    elif soma%2==0 and opção=='I':
        print(f'Você escolheu {jogador} e o computador {computador}. O total deu {soma}, É PAR!')
        break
    else:
        print(f'Você escolheu {jogador} e o computador {computador}. O total deu {soma}, É IMPAR!')
        break
    sleep(1)
    print('PARABÉNS! VOCÊ VENCEU.')
    print('Vamos jogar novamente...')
    print('')
    sleep(1)
if contador<=1:
    print(f'GAME OVER! Você venceu {contador} vez.')
else:
    print(f'GAME OVER! Você venceu {contador} vezes.')
