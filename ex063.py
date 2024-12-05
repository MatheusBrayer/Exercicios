# SEQUENCIA FIBONACCI
print('SEQUENCIA FIBONACCI')
quantidade_de_numeros = int(input('Qunatos números deseja mostrar: '))
print('')

t1=0
t2=1
contador=2

print('{} ⇨ {}'.format(t1, t2), end='')

while contador < quantidade_de_numeros:
    t3 = t1+t2
    print(' ⇨ {}'.format(t3), end='')
    t1=t2
    t2=t3
    contador+=1

print(' ⇨ FIM')