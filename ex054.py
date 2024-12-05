# PROGRAMA ANALISADOR DE MAIORES DE IDADE

import datetime
data = datetime.datetime.now().year

maior = 0
menor = 0

for n in range (1,7):
    ano_nascimento = int(input('Digite a idade da {}° pessoa:'.format(n)))
    idade = data - ano_nascimento
    print('{} anos'.format(idade))
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('\033[32mNo total tivemos {} pessoas maiores de idade\033[m \n\033[31mE {} menores de idade.\033[m'.format(maior,menor))
