from interface import *
from sistema import *
from time import sleep

arquivo='CursoEmVideo.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

while True:
    resp = menu(['opção 1', 'opção 2', 'opção 3'])
    if resp==1:
        cabeçalho('PESSOAS CADASTRATAS')
        ler_arquivo(arquivo)
    elif resp==2:
        cabeçalho('CADASTRO DE PESSOAS')
        nome = str(input('NOME:'))
        idade = leitura('IDADE:')
        cadastro(arquivo, nome, idade)
    elif resp==3:
        print(cores('PROGRAMA FINALIZADO!', vermelho=True))
        break
    elif resp==0:
        break
    else:
        print(cores('ERRO! Digite um número valido.',vermelho=True))
    sleep(2)