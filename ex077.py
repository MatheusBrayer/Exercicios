# PROGRAMA DE VOGAIS

lista=('PYTHON','COMPUTADOR','SOFTWARE','ENGENHEIRO','ESTUDANTE','PROGRAMADOR','RICO','SAUDE')
for palavra in lista:
    print(f'\nNa palavra {palavra} temos', end=' ')
    for vogal in palavra:
        if vogal in 'EIOUA':
            print(vogal.lower(), end=' ')
