aluno={}
aluno['Nome']=str(input('Nome:'))
aluno['Média']=float(input(f'Média de {aluno["Nome"]}:'))
print('='*30)
print(f'- Nome é igual a {aluno["Nome"]}')
print(f'- Média igual a {aluno["Média"]}')
if aluno['Média']<5:
    print('- A situação é reprovado!')
if aluno['Média']>=5 and aluno['Média']<7.5:
    print('- Situação igual a recuperação!')
else:
    print('- Situação Aprovado!')