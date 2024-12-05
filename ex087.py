# MATRIZ APRIMORADA

lista=[[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        lista[l][c]=(int(input(f'Digite um valor para ser inserido na posição [{l},{c}]: ')))
total=0
soma_terceira_coluna=lista[2][0]+lista[2][1]+lista[2][2]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]', end='')
        if lista[l][c]%2==0:
            total+=lista[l][c]
    print()
print('-'*30)
print(f'A soma dos valores pares é {total}')
print(f'A soma dos valores da 3° coluna é {soma_terceira_coluna}')
print(f'O maior valor da 2° linha é {max(lista[1])}')