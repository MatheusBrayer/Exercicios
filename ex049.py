# PROGRAMA 09 ATUALIZADO (TABUADA)

m = int(input('Digite o número que deseja ver a tabuada: '))

for n in range (0, 11):
    print('{:2} x {:2} = {:2}'.format((m), (n), n*m))

