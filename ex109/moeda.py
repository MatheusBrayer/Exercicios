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


def format_moeda(v=0):
    '''
    -> função para formatar valor para o modo moeda
    :param v: valor a ser formatado
    :return: retona valor 'v' formatado.
    '''
    return (f'R${v:.2f}'.replace('.',','))
