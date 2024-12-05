# FUNÇÃO PARA VOTAÇÃO
def voto():
    from datetime import date
    ano_nascimento=int(input('Em que ano você nasceu?'))
    idade=date.today().year-ano_nascimento
    print(f'Com {idade} anos', end=' ')
    if idade>=70:
        print('o voto é opcional!')
    if idade>=17 and idade<70:
        print('o voto é obrigatótio!')
    if idade<17:
        print('não vota!')

voto()