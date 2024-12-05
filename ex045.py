
# JOGO PEDRA, PAPEL, TESOURA

import time
from random import randint

print('''ESCOLHA UMA OPÇÃO 
[0] Pedra
[1] Papel
[2] Tesoura''')

opções = ['Pedra', 'Papel', 'Tesoura']
maquina = randint(0,2)
jogador = int(input('Qual a sua jogada? '))

time.sleep(.5)
print('JO')
time.sleep(.5)
print('KEN')
time.sleep(.5)
print('PO!!!')
time.sleep(.5)

print('-'*40)
print('Computador escolheu {}'.format(opções[maquina]))
print('Jogador escolheu {}'.format(opções[jogador]))
print('-'*40)

if jogador == 0:
    if maquina == 0:
        print('EMPATE')
    elif maquina == 1:
        print('Comptutador Venceu!')
    else:
        print('Jogador Venceu!')

elif jogador == 1:
    if maquina == 0:
        print('Jogador Venceu!')
    elif maquina == 1:
        print('EMPATE')
    else:
        print('Computador Venceu!')

elif jogador == 2:
    if maquina == 0:
        print('Computador Venceu!')
    elif maquina == 1:
        print('Jogador Venceu!')
    else:
        print('EMPATE!')