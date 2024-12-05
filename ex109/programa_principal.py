import moeda


valor=float(input('Digite um valor: R$ '))
print(f'A metade de {moeda.format_moeda(valor)} é igual a {moeda.metade(valor, True)}.')
print(f'O dobro de {moeda.format_moeda(valor)} é igual a {moeda.dobro(valor, True)}.')
print(f'Aumento de 10% é {moeda.aumento(valor,10, True)}.')
