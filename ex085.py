# SEPARAR VALORES PARES E IMPARES EM UMA UNICA LISTA

lista=[]
pares=[]
impares=[]
for p in range(0,7):
    valor=(int(input(f'Digite o {p+1}° valor: ')))
    if valor % 2 == 0:
        pares.append(valor)
    if valor % 2 != 0:
        impares.append(valor)
impares.sort()
pares.sort()
lista.append(pares[:])
lista.append(impares[:])
print('-'*20)
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')