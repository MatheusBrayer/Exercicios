# Converter um numero para Binário, Octal e hexadecimal

numero = int(input('Digite o numero inteiro que deseja converter: '))

print('-------'*12)

print('[1] Para Binário \n[2] Para Octal \n[3] Para Hexadecimal')
escolha = int(input('Escolha qual forma deseja converter:'))

binario = bin(numero)
octal = oct(numero)
hexadecial = hex(numero)

if escolha == 1:
    print('{} convertido para binário é igual a {}.'.format(numero, binario[2:]))

elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(numero, octal[2:]))
elif escolha == 3:
    print('{} convertido para hexadecial é igual a {}'.format(numero, hexadecial[2:]))