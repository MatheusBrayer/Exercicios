import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(co, ca)
print(' a hipotenusa vai medir {:.5}'.format(hip))