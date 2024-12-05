# EXERCICO 84

cadastro=[]
lista=[]
total_cadastrados=0
maior_peso=0
pessoa_maior_peso=[]
menor_peso=0
pessoa_menor_peso=[]
while True:
    total_cadastrados += 1
    cadastro.append(str(input('NOME: ')))
    cadastro.append(int(input('PESO: ')))
    if total_cadastrados == 1:
        menor_peso=maior_peso=cadastro[1]
    lista.append(cadastro[:])
    cadastro.clear()
    resp=str(input('Deseja continuar? ')).upper().strip()[0]
    if resp in 'N':
         break
print(lista)
for p in lista:
    print(p[1])
    if p[1]>=maior_peso:
        if p[1]>maior_peso:
            pessoa_maior_peso.clear()
        maior_peso=p[1]
        pessoa_maior_peso.append(p[0])
    if p[1]<=menor_peso:
        if p[1]<menor_peso:
            pessoa_menor_peso.clear()
        menor_peso=p[1]
        pessoa_menor_peso.append(p[0])
print(f'Foram cadastradas um total de {total_cadastrados} pessoas.')
print(f'A pessoa com maior peso foi {pessoa_maior_peso} com {maior_peso}KG.')
print(f'A pessoa com menor peso foi {pessoa_menor_peso} com {menor_peso}KG.')
