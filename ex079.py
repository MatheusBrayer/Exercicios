# LISTA ORDENADA

lista=[]
while True:
    add=(input('Digite um valor: '))
    if add not in lista:
        lista.append(add)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, NÂO será adicionado!')
    continuar=str(input('Quer continuar? ')).upper().strip()[0]
    if continuar=='N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')

