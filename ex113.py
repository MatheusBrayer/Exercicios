def leiaInt(n):
    while True:
        try:
            valor=int(input(n))
            return valor
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Pro favor digite um número inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mUsuário encerrou o programa manualmente!\033[m')


def leiaFlout(n):
    while True:
        try:
            valor = float(input(n))
            return valor
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Pro favor digite um número real valido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mUsuário encerrou o programa manualmente!\033[m')


v1=leiaInt('Digite um valor inteiro: ')
v2=leiaFlout('Digite um valor real:')
print(f'\n\033[1;32mO valor inteiro digitado foi {v1} e o ral foi {v2}.')