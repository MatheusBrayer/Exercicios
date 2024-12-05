# CADASTRO DE TRABALHADOR
from datetime import date

funcionario={'nome':(str(input('Nome:'))),
             'ano':date.today().year-(int(input('Ano de nescimento:'))),
             'carteira': int(input('Numero da carteira de trabalho [0 não tem]:'))}
if funcionario['carteira']!=0:
    funcionario['contratação']=int(input('Ano de contratação:'))
    funcionario['salario']=float(input('Salário: R$'))
    funcionario['aposentadoria']=(30-((date.today().year)-(funcionario['contratação'])))+funcionario['ano']
print(funcionario)
print(date.today().year)
print('=-'*30)
for k, v in funcionario.items():
    print(f'    -{k} igual à {v}')