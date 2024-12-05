# CADASTRO DE PESSOAS
total_idade = 0
mais_velho = int(0)
nome_mais_velho = 0
feminino = 0

for p in range (1, 5):
    print('-'*5,'{}° Pessoa'.format(p),'-'*5)
    nome = input('Nome:')
    idade = float(input('Idade:'))
    sexo = input('Sexo [M/F}:').upper()
    total_idade += idade

    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome.title()

    if sexo == 'F' and idade <= 20:
        feminino += 1


média_idade = total_idade / 4
print('A média de idade do grupo é {} anos.'.format(média_idade))
print('O homem mais velho tem {} e se chama {}.'.format(int(mais_velho), nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(feminino))