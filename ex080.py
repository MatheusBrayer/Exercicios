# LISTA ORDENADA SEM .SORT()
lista=[]
posição=0

for v in range(0,5):
    valor_add=int(input('Digite um valor:'))
    if v==0 or valor_add>lista[-1]:
        lista.append(valor_add)
        print('Adicionado')
    else:
        pos=0
        while True:
            if valor_add<=lista[pos]:
                lista.insert(pos, valor_add)
                print('Adicionado')
                break
            pos += 1
    print(lista)

