n = input('digite seu nome completo: ')

print('Analisando seu nome...\n ')
print('Seu nome com as letras maiusculas fica - {} '.format(n.upper()))
print('Seu nome com as letras minusculas fica - {}'.format(n.lower()))
separado = n.split()
junto = ''.join(separado)
print('Seu nome completo tem {} letras'.format(len(junto)))
print('Seu primeiro nome {} tem {} letras'.format(separado [0], len(separado [0])))
