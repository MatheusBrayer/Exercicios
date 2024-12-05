# EXERCICIO PARA FATORIAL DE UM NUMERO

num = int(input('Digiteo número que deseja calcular o fatorial:'))
cont = num
print('Calculando fatorial de \033[32m{}\033[m...'.format(num))

while cont != 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont>1 else' = ',end='')
    num = num * (cont-1)
    cont -= 1
print('\033[32m{}\033[m'.format(num))



