import datetime

ano_atual = datetime.datetime.now().year
nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - nascimento
anos_faltam = ano_atual - nascimento - 18
ano_alistamento = ano_atual - anos_faltam

print('Quem nasceu no ano {} faz {} anos no ano de {}'.format(nascimento, idade, ano_atual))

if idade < 18:
    print('''Seu ano de alistamento é {}.
Ainda falta {} para se alistar.'''.format(ano_alistamento, str(anos_faltam)[1:]))

elif idade > 18:
    print('''Você já deveria ter se alistado a {} anos.
Seu ano de alistamento foi em {}. '''.format(anos_faltam, ano_alistamento))

elif idade == 18:
    print('''Você deve se alistar esse ano ainda.''')