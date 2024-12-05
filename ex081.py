lista=[]
while True:
    n=int(input('Digite um valor: '))
    lista.append(n)
    continuar=input('Deseja continuar?[N/S] ').upper().strip()[0]
    if continuar in 'N':
        break
lista.sort(reverse=True)
print(f'Os valores digitados em ordem crescente {lista}')
if '5' in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
print(f'Você digitou {len(lista)} elementos')