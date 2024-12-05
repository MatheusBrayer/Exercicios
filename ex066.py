# INSERÇÃO DE NUMEROS COM PARADA


soma=contador=número=0
while True:
    número = int(input('Digite um número (999 para parar): '))
    if número==999:
        break
    soma += número
    contador += 1
print(f'A soma dos {contador} é igual a {soma}.')