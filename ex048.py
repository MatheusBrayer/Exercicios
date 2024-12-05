# PROGRAMA QUE SOMA TODOS OS NUMEROS MULTIPLOS DE 3 ENTRE 1 E 500
s = 0
m = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
        s = s+1
        m = m + n


print('A soma de todos os {} valores é {}'.format(s, m))




