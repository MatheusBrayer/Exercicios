frase = str(input('Digite uma frase: ')).strip().lower()

print('A letra A aparece {} vezes na sua frase.'.format(frase.count('a')))

print('A letra A aparece a prieira vez na posição {} e a ultima vez na posição {}.'.format(frase.find('a')+1, frase.rfind('a')+1))