# progressão aritimética

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 0
final = 10
total_PA = 0
while contador < final:
    print(termo, end=' → ')
    contador += 1
    termo += razão
    total_PA+=1
    if contador == 10:
        print('PAUSA')
    while contador == 10:
        print('')
        proximos_PA = int(input('Quantos termos deseja ver a mais? '))
        PA = termo + (proximos_PA)*razão
        for continuação in range (termo, PA, razão):
            print(continuação, end=' → ')
            termo+=razão
            total_PA+=1
        print('PAUSA')
        if proximos_PA == 0:
            contador+=1
print('Progressão total com {} termos mostrados.'.format(total_PA))
