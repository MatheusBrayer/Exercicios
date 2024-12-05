# REFAZENDO O EXERCICO 51

print('='*10,'Gerador de PA','='*10)
print('')
num = int(input('Primeiro termo:'))
razão = int(input('Razão:'))
cont = 0

while cont < 10:
    print(num, end=' → ')
    cont += 1
    num += razão

print('FIM')