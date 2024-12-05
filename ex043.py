# EXERCICIO PARA CALCULAR IMC

p = float(input('Qual seu peso (kg): '))
a = float(input('Qual sua altura (m): '))

imc = p / (a**2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal.')
elif 18.5 < imc < 25:
    print('Você está com o peso IDEAL.')
elif 25 < imc < 30:
    print('Você está com SOBREPESO.')
elif 30 < imc < 40:
    print('Você está com OBESIDADE.')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA.')