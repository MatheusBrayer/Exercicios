# PROGRAMA DE NUMEROS PRIMOS
s=0
numero = int(input('Digite um número:'))

for n in range (1, numero+1):
    if numero % n == 0:
        s+=1
        print('\033[32m{}\033[m'.format(n), end=' ')
    elif numero != 0:
        print('\033[31m{}\033[m'.format(n), end=' ')
print()
print('O numero {} foi divisivel {} vezes.'.format(numero,s))

if s == 2:
    print('Por isso ele é PRIMO')
else:
    print('por isso ele NÃO É PRIMO')