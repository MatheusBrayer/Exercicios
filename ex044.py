# SIMULADOR DE PREÇO PARA LOJA

print('{:=^50}'.format(' LOJAS MATHEUS '))

valor = float(input('Digite o valor das suas compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] À VISTA NO DINHEIRO
[2] À VISTA NO CARTÃO
[3] 2X NO CARTÃO
[4] 3X NO CARTÃO''')

n1 = valor - (valor*10/100)
n2 = valor - (valor*5/100)
n4 = valor + (valor*20/100)

pagamento = int(input('Qual a forma de pagamento?'))

if pagamento == 1:
    print('Sua compra de R${}, com desconto de 10% vai custar R${} no final'.format(valor, n1))
elif pagamento == 2:
    print('Sua compra de R${}, com desconto de 5% vai custar R${} no final'.format(valor, n2))
elif pagamento == 3:
    print('''Sua compra será parcelada em 2x sem juros
Com parcelas de R${:.2f}'''.format(valor/2))
elif pagamento == 4:
    parcelas = int(input('Digite a quantidade de parcelas:'))
    juros = valor + (valor*20/100)
    print('''Sua compra será parcelada em {}x com acrescimo de 20%.
valor das parcelas fica em R${} com valor total de R${}'''. format(parcelas,juros/parcelas, juros))
else:
    print('\033[31mOpção invalida, TENTE NOVAMENTE!\033[m')