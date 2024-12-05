# ANALISE DE JOGADOR

jogador= {'nome':(input('Nome:'))}
gols=[]
total=0
partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(0,partidas):
    p=(int(input(f'Quantos gols na partida {p+1}:')))
    gols.append(p)
    total+=p
jogador['gols']=gols[:]
jogador['total']=total
print('=-'*30)
print(jogador)
print('=-'*30)
for item, valor in jogador.items():
    print(f'o {item} tem valor {valor}.')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for partida, gol in enumerate(gols):
    print(f'    => Na partida {partida+1} ele fez {gol} gols.')