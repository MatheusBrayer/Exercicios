#Programa para converter real em dolar
real = float(input('Digite quantos reais vc tem? R$ '))

dolar = real/3.27

print('Você pode comprar ${:.2f} dolares com R${} reais'.format(dolar, real))
