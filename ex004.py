n = input('Digite algo: ')

print(type(n))
print('Ele contem somente letras e numeros?',n.isalnum())
print('Ele tem somente letras alfabeticas?',n.isalpha())
print('Ele tem só letras minusculas?',n.islower())
print('Ele tem só numes decimais?',n.isdecimal())
print('Ele está capitalizado?',n.istitle())
print('Ele tem sò letras maùsculas?',n.isupper())
print('Ele tem somente espaços: ',n.isspace())