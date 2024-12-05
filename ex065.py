# EXERCICIO DE MAIOR E MENOR VALOR + SOMA

continuar = True
contagem = 0
soma = 0
maior=0
menor=0
while continuar == True:
    número = int(input('Digite um número: '))
    decisão = str(input('Deseja continuar [S/N]:')).upper().strip()
    contagem += 1
    soma += número
    if contagem ==1:
        maior=número
        menor=número
    else:
        if maior < número:
            maior=número
            maior=número
        if menor > número:
            menor=número
    if decisão == 'N':
        continuar=False
    elif decisão == 'S':
        continuar=True
    else:
        decisão_2 = True
        while decisão_2 == True:
            print('Valor invalido!')
            decisão_3 = str(input('Deseja continuar [S/N]:')).upper().strip()
            if decisão_3 != 'S' and decisão_3 != 'N':
                decisão_2 = True
            elif decisão_3 == 'S':
                decisão_2=False
            else:
                decisão_2 = False
                continuar = False
média=soma/contagem
print('Você digitou {} números e a média deles deu {:.2f}'.format(contagem, média))
print('O número maior foi {} e o menor foi {}'.format(maior, menor))