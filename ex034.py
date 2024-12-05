salario = float(input('Digete o valor do sálario do funcionário: R$'))

if salario > 1250:
    aumento = (salario * 10 / 100) + salario
else:
    aumento = (salario * 15 / 100) + salario

print('Quem ganha R${:.2f} passará a ganhar R${:.2f}'.format(salario, aumento) )