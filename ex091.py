# JOGO DE DADOS
from random import randint
from time import sleep
from operator import itemgetter

jogo={'jogador1':randint(0,6),'Jogador2':randint(0,6),'Jogador3':randint(0,6),'jogador4':randint(0,6)}
for i, v in jogo.items():
    print(f'O {i} tirou {v}')
    sleep(1)
print('=-'*30)
print(f'{"RANKING DE PONTOS":^50}')
ordem=sorted(jogo.items(), key=itemgetter(1), reverse=True) # para colocar em ordem, 'reverse' para ser decrescente
for i,v in enumerate(ordem):
    print(f'       O {i+1}° lugar ficom com: {v[0]} com {v[1]}.')
    sleep(1)