# validação de numero

def LeiaInt(msg):
    print('-'*30)
    while True:
        func = input(msg)
        if func.isnumeric():
            return func
            break
        else:
            print('\033[1;31m ERRO! Digite um número inteiro valido.\033[m')


n= LeiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}.')