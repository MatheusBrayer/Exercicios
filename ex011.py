#Programa para calcular quantidade de tinta para pintar determinada área
l = float(input('Qual a largura da sua parede em metros? '))
a = float(input('Qual a altura da sua parede em metros? '))

area = l*a

latas = area/2

print('para pintar {} m² será preciso ter {} latas de tintas'.format(area, latas))
