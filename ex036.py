# Cálculo de empréstimo

valor_casa = float(input('Digite o valor do imóvel que deseja comprar: R$ '))
sálario = float(input('Qual o valor da sua renda mensal: R$ '))
percelas = float(input('Em quantos anos deseja pagar o imóvel: '))

valor_parcela = valor_casa/(percelas*12)
limete_parcela = sálario*30/100
print('O valor maxímo que sua parcela pode chegar é de R${:.2f}'.format(limete_parcela))
print('O valor da parcela ficaria R$ {:.2f}'.format(valor_parcela))

if valor_parcela => limete_parcela:
    print('O valor da parcela ultrapassa os 30% da sua renda mensal. \nEmpréstimo NEGADO!')

else:
    print('O valor da parcela está dentro dos 30% da sua renda mensal. \nEmprestimo APROVADO!')
