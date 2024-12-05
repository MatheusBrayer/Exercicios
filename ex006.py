#Programa para saber o dobro, triplo e raiz de um número
n = int(input('Digite um numero: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2)

print('O dobro de {} é {}'.format(n, dobro))
print('O triplo de {} é {}'.format(n, triplo))
print('A raiz quadrada de {} é {}'.format(n, raiz))