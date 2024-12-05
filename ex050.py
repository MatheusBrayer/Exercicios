# PROGRAMA DE SOMA DE NUMEROS PARES
s = 0
for n in range (1, 7):
    m = int(input('Digite o {} numero:'.format(n)))
    if m % 2 == 0:
        s += m

print('A soma de todos os numeros pares é {}.'.format(s))