# PRINT ADAPTAVEL

def escreva(msg):
    print('-'*(len(msg)+6))
    print(f'{msg:^{len(msg)+6}}')
    print('-'*(len(msg)+6))


frase='oi!'
escreva(frase)