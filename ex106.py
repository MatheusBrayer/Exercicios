# PROGRAMA HELP PYTHON
from time import sleep
def ajuda(biblioteca):
    print('\033[46;97m~' * 50)
    print(f'{f"Acessando manual do comando {biblioteca}":^50}')
    print('~' * 50)
    sleep(1)
    print('\033[107;30m')
    return help(biblioteca)
    print('\033[m')

while True:
    print('\033[43;97m~'*50)
    print(f'{"SISTEMA DE AJUDA PYTHON":^50}')
    print('~'*50)
    opc=(input('\033[mFunção ou Biblioteca:')).strip().lower()
    if opc in 'sair':
        print('\033[41;97mPROGRAMA FINALIZADO!')
        break
    else:
        ajuda(opc)