# NUMEROS EM UMA TUPLA

numeros=(int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o ultimo número: ')))
print('='*20)
print(numeros)
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}° posição.')
else:
    print('O número 3 não foi digitado.')
print('Os números pares digitados foram: ', end='')
for pares in numeros:
    if pares%2==0:
        print(pares, end=', ')
