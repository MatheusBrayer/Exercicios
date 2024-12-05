# exercidio 28 melhorado

import random

print('''Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
será que você consegue adivinhar?''')

acertou = False
computador = random.randint(0,10)
contador = 0

while not acertou:
    jogador = int(input('Qual seu palpite?'))
    contador += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais, tente novamente!')

        elif jogador > computador:
            print('Menos, tente novamente!')

print('\033[1;32mVocê acertou com {} tentativas. PARABÉNS!\033[m'.format(contador))
