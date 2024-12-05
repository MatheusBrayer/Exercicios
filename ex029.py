velocidade = int(input('Qual velocidade o carro está?'))

multa = f"R${(velocidade - 80)*7},00"

if velocidade > 80:
    print('Você exedeu o limite de velocidade! \nSua multa é de {}'. format(multa))
else:
    print('Você está dentro do limite permitido')
print('tenha um ótimo dia e dirija com cuidado!'.upper())