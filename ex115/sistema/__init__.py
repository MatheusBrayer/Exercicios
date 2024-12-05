import interface

def arquivo_existe(arqv):
    try:
        arquivo=open(arqv, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(txt):
    try:
        arquivo=open(txt, 'wt+')
        arquivo.close()
    except:
        print('Erro ao criar arquivo!')
    else:
        print('Arquivo criado com sucesso!')


def ler_arquivo(arqv):
    try:
        a=open(arqv, 'rt')
    except:
        print(interface.cores('Erro ao ler arquivo!', vermelho=True))
    else:
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastro(arqv, nome='Desconhecido', idade=0):
    try:
        a=open(arqv, 'at')
    except:
        print(interface.cores('Erro ao abrir o arquivo!', vermelho=True))
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(interface.cores(f'Erro ao cadastrar {nome}.'))
        else:
            print(f'{nome} cadastrado com sucesso!')
            a.close()

