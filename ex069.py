# CADASTRO DE PESSOAS

quantidade_maiores=homens=mulheres_maiores=0
while True:
    idade=int(input('Idade:'))
    if idade>=20:
        quantidade_maiores+=1
    sexo=str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo=str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo=='M':
        homens+=1
    if sexo=='F' and idade<=18:
        mulheres_maiores+=1
    continuar=str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar=='N':
        break
print(f'A quantidade de pessoas maiorores de 18 anos é {quantidade_maiores}.')
print(f'Temos um total de {homens} homens cadastrados.')
print(f'Temos um total de {mulheres_maiores} mulheres com menos de 20 anos.')