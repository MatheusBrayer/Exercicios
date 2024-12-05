import sistema
def linha(l=45):
    print('-'*l)


def cabeçalho(txt):
    linha()
    print(txt.center(45))
    linha()


def leitura(msg):
    while True:
        try:
            v=int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31m\nUsuário interrompeu programa manualmente!\033[m')
            return 0
        else:
            return v


def menu(lista):
    cabeçalho(cores('MENU PINCIPAL', amarelo=True))
    c=1
    for l in lista:
        print(f'{cores(c, amarelo=True)} - {cores(l, azul=True)}')
        c+=1
    linha()
    opc=leitura(cores('Digite opção desejada:', azul=True))
    return opc


def cores(txt,vermelho=False, amarelo=False, azul=False):
    if amarelo==True:
        return(f'\033[1;33m{txt}\033[m')
    if vermelho==True:
        return(f'\033[1;31m{txt}\033[m')
    if azul==True:
        return(f'\033[1;36m{txt}\033[m')




