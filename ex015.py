dias_alugados = int(input('Quantos dias ficou com o carro? '))
km_rodados = float(input('Quantos km andou? '))

valor_total = (60*dias_alugados) + (0.15*km_rodados)

print('O valor total a ser pago é de R${:.2f}'.format(valor_total))
