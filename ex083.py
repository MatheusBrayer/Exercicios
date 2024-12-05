# VALIDANDO EXPRESÃO

expressão=str(input('Digite a expresão: '))
abertos=expressão.count('(')
fechados=expressão.count(')')

if abertos==fechados:
    print('Expressão valida!')
else:
    print('Expressão Invalida!')

