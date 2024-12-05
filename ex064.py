n1 = int(input('Digite um número [999 para parar]:'))
contador=0
somatória=0
while n1 != 999:
    n2 = int(input('Digite um número [999 para parar]:'))
    contador+=1
    somatória+=n1
    n1=n2

print('Você digitou {} numeros e a soma deles é {}.'.format(contador,somatória))