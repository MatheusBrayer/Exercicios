#Programa para calcular média de duas notas
nota1 = float(input('Digite o valor da primeira nota: '))
nota2 = float(input('Digite o valor da segunda nota: '))

media = (nota1 + nota2)/2
print('A média das notas é {:.1f}'.format(media))
# :.1f significa 'depois do ponto flutuante coloque apenas 1 valor'.
