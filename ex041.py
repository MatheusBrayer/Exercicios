# Exercicio para classificar a categoria que o atleta vai se encaixar

# importando a biblioteca para verificar o ano atual
from datetime import date

#ano de nascimento da pessoa
ano = int(input('Digite o ano de nascimento: '))

# data atual
data = date.today().year

#idade da pessoa
idade = data - ano

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM.')

elif idade <= 14:
    print('Classificação: INFÂNTIL.')

elif idade <= 19:
    print('Classificação: JUNIOR.')

elif idade <= 25:
    print('Classificação: SENIOR.')

elif idade > 26:
    print('Classificação: MASTER.')


