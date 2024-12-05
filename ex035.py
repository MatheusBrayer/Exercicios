print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)

n1 = int(input('primeiro segmento:'))
n2 = int(input('Segundo segmento:'))
n3 = int(input('Terceiro segmento:'))

if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print('Os segmentos acima PODEM formar um triangulo retangulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triangulo retangulo')