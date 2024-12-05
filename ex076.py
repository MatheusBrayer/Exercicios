#LISTA DE PREÇOS

lista=('caderno', 10.50,
       'lápis', 1.50,
       'estojo', 5.40,
       'mochila', 52,
       'caneta', 2.50,
       'borracha', 0.5,)

print('-'*40)
print(f'{"LISTA DE PREÇO":^40}')
print('-'*40)
for item in range(0,len(lista)):
    if item%2==0:
        print(f'{lista[item]:.<30}',end='')
    else:
        print(f'R${lista[item]:>6.2f}')
print('-'*40)