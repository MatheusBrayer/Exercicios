# DETECTOR DE PALINDROMO

frase = input('Digite uma frase:').strip()
normal = ''.join(frase.upper().split())
invertida = ''.join(frase[::-1].upper().split())

print('O inverso de {} é {}'.format(normal, invertida))
if normal == invertida:
    print('Temos uma palindromo')
else:
    print('Isso não é um palindromo')