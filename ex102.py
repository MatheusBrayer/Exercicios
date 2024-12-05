# programa fatorial


def fatorial(num, show=True):
    '''
    -> Calculo de fatorial de um numero
    :param num: numero que deseja ver o fatorial
    :param show: para mostrar ou não o calculo (opcional)
    :return: retorna valor do calculo de fatorial
    '''
    fat = 1
    print(f'{num}! = ', end='')
    for f in range(num,0,-1):
        if show:
            if f > 1:
                print(f'{f} x ',end='')
            if f == 1:
                print(f'{f} = ', end='')
        fat*=f
    return fat



print(fatorial(5, show=True))
#help(fatorial)