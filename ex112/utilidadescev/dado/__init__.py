def leia_dinheiro(v):
    validacao=True
    while validacao==True:
        msg=str(input(v).replace(',','.').strip())
        if msg.isalpha() or msg in '':
            print(f'\033[31mERRO! \'{msg}\' não é um numero valido!\033[m')
        else:
            return float(msg)
            validacao=False

