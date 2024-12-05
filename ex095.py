# ANALISE DE JOGADOR APRIMORADA
time=[]
jogador={}
while True:
    jogador.clear()
    jogador['nome']= str(input('Nome:'))
    gols=[]
    total=0
    partidas=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0,partidas):
        p=int(input(f'Quantos gols na partida {p+1}:'))
        gols.append(p)
        total+=p
    jogador['gols']=gols[:]
    jogador['total']=total
    time.append(jogador.copy())
    while True:
        opc = str(input('Deseja cadastrar outro jogado?[S/N] ')).upper().strip()[0]
        if opc in 'NS':
            break
        print('Valor inavalido!')
    print('-'*50)
    if opc=='N':
        break
# tabela dos jogadores
print(f'{"Cod":<5}{"Nome":^15}{"Gols":^15}{"Total":^5}')
print('-'*50)
for j, k in enumerate(time):
    print(f'{j:^5}{k["nome"]:<15}{str(k["gols"]):<15}{k["total"]:^5}')
print()
# informações do jogador
print(f'quantidade {len(time)}')
while True:
    opc=int(input('Digite o código do jogador que deseja ver mais informações [999 cancela}:'))
    if opc==999:
        break
    if opc<len(time):
        print('-'*50)
        print(f'Levantamento do jogador {time[opc]["nome"]}')
        print('-'*50)
        for p, k in enumerate(time[opc]['gols']):
            print(f'Fez {k} no jogo {p}.')
    else:
        print('Não existe jogador para esse código, TENTE NOVAMENTE!')