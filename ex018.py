import math
ang = float(input('Digite o valor do angulo: '))

#para transformar graus em radianos
ang_rad = math.radians(ang)

co = math.cos(ang_rad)
se = math.sin(ang_rad)
tang = math.tan(ang_rad)

print('Os valores são: \n'
      'Cosseno é igual a {:.3} \n'
      'Seno é igual a {:.3} \n'
      'Tangente é igual a {:.3}'.format(co,se,tang))