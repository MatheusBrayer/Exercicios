# REPITINDO OS 10 TERMOS DE UMA PA

print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

termo = int(input('Primeiro termo:'))
razão = int(input('razão: '))
décimo = termo + (10-1)*razão

for n in range (termo, décimo+razão, razão): # NUMERO INICIAL, ATÉ O NUMERO FINAL, PULANDO DE QUANTO EM QUANTO
    print(n, end=' → ')
print('ACABOU!')