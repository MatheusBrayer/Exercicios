def metade(v=0, formatação=False):
    '''
    -> função para dividir valor por 2.
    :param v: valor informado pelo cliente
    :param formatação: True para adicionar formatação de moeda
    :return: retorna metade do valor de 'v'
    '''
    v /= 2
    return v if formatação is False else format_moeda(v)    # se formatação for falso ele não aplica o modo 'format_moeda'


def dobro(v=0, formatação=False):
    '''
    -> função para dobrar valor
    :param v: valor a ser dobrado
    :param formatação: True para adicionar formatação de moeda
    :return: retorna valor dobrado de 'v'
    '''
    v *= 2
    return v if formatação is False else format_moeda(v)


def aumento(v=0, p=10, formatação=False):
    '''
    -> função para aumentar em % o valor de 'v'.
    :param v: valor a ser aumentando
    :param p: porcentagem que irá aumentar
    :param formatação: True para adicionar formatação do modo moeda
    :return: retona valor de 'v' aumentado 'p'%.
    '''
    v = ((v*p)/100)+v
    return v if formatação is False else format_moeda(v)


def redução(v=0, r=0, formatação=False):
    '''
    -> função para diminuir em % volor de 'v'
    :param v: valor a ser diminuido
    :param r: porcentagem da redução
    :param formatação: True para formatação no modo moeda
    :return: retorna 'v' com a redução de 'r'%.
    '''
    v=v-(v*r/100)
    return v if formatação is False else format_moeda(v)


def format_moeda(v=0):
    '''
    -> função para formatar valor para o modo moeda
    :param v: valor a ser formatado
    :return: retona valor 'v' formatado.
    '''
    return (f'R${v:.2f}'.replace('.',','))


def resumo(v,a,r):
    '''
    -> função para um resumo de calculo de valores
    :param v: valor para se obter o resumo
    :param a: porcentagem de aumento do valor 'v'
    :param r: porcentagem de redução do valor 'v'
    :return: retorna um resumo dos calculos de 'v'
    '''
    print('-'*36)
    print(F'{"RESUMO DO VALOR":^36}')
    print('-'*36)
    print(f'Preço analisado: \t\t{format_moeda(v)}') # \t é uma tabulação, mesma coisa que tecla taabe
    print(f'Dobro do preço: \t\t{dobro(v, True)}')
    print(f'Metade do preço: \t\t{metade(v, True)}')
    print(f'{a}% de aumento preço: \t{aumento(v,a, True)}')
    print(f'{r}% de redução preço: \t{redução(v,r, True)}')

