import moeda


valor=float(input('Digite um valor: R$ '))
print(f'A metade de {moeda.format_moeda(valor)} é igual a {moeda.format_moeda(moeda.metade(valor))}.')
print(f'O dobro de {moeda.format_moeda(valor)} é igual a {moeda.format_moeda(moeda.dobro(valor))}.')
print(f'Aumento de 10% é {moeda.format_moeda(moeda.aumento(valor))}.')