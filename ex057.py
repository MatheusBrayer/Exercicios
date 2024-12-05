# EXERCICIO PARA VERIFICAR GENERO

genero = str(input('Digite seu sexo [M/F]:')).upper().strip()[0]

while genero not in 'MmFf':
    sexo = str(input('OPÇÃO ONVALIDA! Tente novamente:')).upper().strip()[0]
    genero = sexo

print('Sexo {} registrado com sucesso!'.format(genero))