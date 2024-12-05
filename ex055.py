# PROGRAMA PARA VER MAIOR E MENOR PESSO ENTRE PESSOAS
maior = 0
menor = 0

for n in range(1, 6):
    peso = int(input('Peso da {}° pessoa:'.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if menor > peso:
            menor = peso

        if maior < peso:
            maior = peso

print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
