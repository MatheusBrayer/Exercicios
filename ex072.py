# PROGRAMA QUE ESCREVE NUMERO POR EXTENSO

num = ('zero', 'um', 'dois', 'tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    numero_escolhido = int(input('NUMERO INVALIDO! Digite um numero entre 0-20:'))
    if numero_escolhido <= 20:
        break
print(f'Você digitou o número "{num[numero_escolhido]}".')
while True:
    continuação = str(input('Deseja escolher outro número [S/N]:')).upper().strip()[0]
    while continuação=='S':
        numero_escolhido = int(input('Digite um numero entre 0-20:'))
        print(f'Você digitou o número "{num[numero_escolhido]}".')
        if numero_escolhido <= 20:
            break
    if continuação=='N':
        print('Programa finalizado!')
        break
