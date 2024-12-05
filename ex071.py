# SIMULADOR DE CAIXA ELETRONICO

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
divisão=resto=saque=0
while True:
    saque=int(input('Qual valor deseja sacar? R$'))
    print('='*30)
    if saque>=50:
        divisão=int(saque/50)
        resto=saque-(divisão*50)
        print(f'{divisão} células de R$50,00')
    if resto>=20:
        divisão = int(resto / 20)
        resto = resto-(divisão * 20)
        print(f'{divisão} células de R$20,00')
    if resto>=10:
        divisão = int(resto / 10)
        resto = resto - (divisão * 10)
        print(f'{divisão} células de R$10,00')
    if resto>=1:
        divisão = int(resto / 1)
        resto = resto - (divisão * 1)
        print(f'{divisão} células de R$1,00')
    print('=' * 30)
    break
print('Volte sempre ao Banco CEV, tenha um bom dia!')