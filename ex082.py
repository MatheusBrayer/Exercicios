# DIVIDINDO VALORES EM LISTAS
lista=[]
pares=[]
impares=[]
escolha=True
while escolha==True:
    valor=int(input('Digite um valor: '))
    if valor%2!=0:
        lista.append(valor)
        impares.append(valor)
    else:
        lista.append(valor)
        pares.append(valor)
    while True:
        continuar=str(input('Deseja continuar? ')).upper().strip()[0]
        if continuar in 'S':
            break
        elif continuar in 'N':
            escolha=False
            break
print('=-'*20)
print(f'Lista completa {lista}')
print(f'Lista de impares {impares}')
print(f'Lista de pares {pares}')
print('=-'*20)