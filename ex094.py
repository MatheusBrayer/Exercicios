# CADASTRO DE PESSOAS

lista=[]
pessoa={}
opc=True
while opc==True:
    pessoa['nome']=str(input('Nome:'))
    while True:
        pessoa['sexo']=str(input('Sexo [M/F]:')).upper().strip()[0]
        if pessoa['sexo'] not in 'MF':
            print('Opção inavalida! Tente novamente!')
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade']=int(input('Idade: '))
    lista.append(pessoa.copy())
    pessoa.clear()
    while True:
        opc2=str(input('Quer continuar [S/N]? ')).upper().strip()[0]
        if opc2 not in 'NS':
            print('Opção inavalida! Tente novamente!')
        if opc2 in 'S':
            print('=-'*30)
            break
        if opc2 in 'N':
            print('=-'*30)
            opc=False
            break
# total de pessoas
print(f'A) O total de pessoas cadastradas é {len(lista)}')
# média de idade
media_idade=0
for t in lista:
    media_idade+=t['idade']
media_idade=float(media_idade/len(lista))
print(f'B) A média de idade é de {media_idade:.1f} anos.')
# mulheres cadastradas
print('C) As mulheres cadastradas foram', end='')
for i in lista:
    if i['sexo'] in 'F':
        print(f', {i["nome"]}', end='')
# Pessoas acima da média
print('\nD) Lita de pessoas com idade acima da média:')
for i in lista:
    if i['idade']>media_idade:
        print(f'        Nome = {i["nome"]}; Sexo = {i["sexo"]}; Idade = {i["idade"]}')

