n = str(input('Digite seu nome completo:')).strip().upper()

print('É um prazer te conhecer {}!'.format(n))

separado = n.split()

print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu ultimo nome é {}'.format(separado[len(separado)-1]))

