import moeda


valor=float(input('Digite um valor: R$ '))
print(f'A metade de R${valor:.2f} é igual a R${moeda.metade(valor):.2f}.')
print(f'O dobro de R${valor:.2f} é igual a R${moeda.dobro(valor):.2f}.')
print(f'Aumento de 10% é R${moeda.aumento(valor):.2f}.')