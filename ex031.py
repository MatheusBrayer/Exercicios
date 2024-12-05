km = int(input("qual a distância da sua viajem:"))

if km < 200:
    preço = km * .5
    print(f'Sua viagem custará R${preço}0')
else:
    preço = km * .45
    print(f'Sua viagem custá R${preço}0')