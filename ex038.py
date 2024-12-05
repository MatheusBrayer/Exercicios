# Programa que compara numeros e fala qual é maior

num1 = int(input('Digite o prmeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print('\033[1;35m O PRIMEIRO número é MAIOR!\033[m')
elif num2 > num1:
    print('\033[1;97m O SEGUNDO número é MAIOR!\033[m')
elif num2 == num1:
    print('1\033[1;33m Os dois números são IGUAIS!\033[m')