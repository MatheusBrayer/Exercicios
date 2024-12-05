# FICHA DO JOGADOR
def jogador(n=0, g=0):
    print(f'O jogador {n} fez {g} gol(s) no ano.')


nome=input('Nome do jogador:')
gols=input('Gols do jogador:')
if nome=='':
    nome='<desconhecido>'
if gols.isdigit():
    gols=int(gols)
else:
    gols=0
jogador(nome, gols)