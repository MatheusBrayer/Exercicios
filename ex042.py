# ANALISADOR DE TRIANGULOS

print('-'*30)
print('ANALISADOR DE TRIANGULOS')
print('-'*30)

n1 = int(input('Digite o primeiro segmento: '))
n2 = int(input('Digite o segundo segmento: '))
n3 = int(input('Digite o terceiro segmento: '))

if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    if n1 == n2 == n3:
        print('Triângulo Equilatero')
    elif n1 != n2 != n3 != n1:
        print('Triângulo Escaleno')
    elif n1 != n2 == n3 or n1 == n2 != n3 or n1 == n3 != n2:
        print('Triângulo Isóceles')
else:
    print('\033[31mEsses valores NÃO formam um triangulo retângulo.\033[m')