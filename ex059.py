# PROGRAMA MENU DE INTERAÇÃO

from time import sleep

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
sair = False

while not sair:
    print('=' * 30)
    print('[1] Soma')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')
    print( '=' * 30)
    opção = int(input('>>>> Qual a sua Opção:'))


    if opção == 1:
        soma = n1 + n2
        print('O resultado de {} + {} é {}'.format(n1, n2,soma))

    elif opção == 2:
        multiplicação = n1 * n2
        print('O resultado da multiplicação entre {} e {} é {}'.format(n1, n2, multiplicação))

    elif opção == 3:
        if n1 < n2:
            print('O maior numero é {}'.format(n2))
        else:
            print('O maior numero é {}'.format(n1))

    elif opção == 4:
        print('Informe os números novamente:')
        n3 = int(input('Primeiro valor:'))
        n4 = int(input('Segundo valor:'))
        n3 = n1
        n4 = n2

    elif opção == 5:
        sair = True
        print('Finalizando...')

    else:
        print('\033[1;31mValor invalido\033[m')
    sleep(2)

print('\033[1;31mPrograma encerrado!\033[m')