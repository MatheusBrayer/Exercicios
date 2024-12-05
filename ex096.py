# calculo de área usando função
print('CONTROLE DE TERRENOS')
print('-'*20)

def calculo_area(larg,comp):
    area=larg*comp
    print(f'A área total de um terreno de {l}m largura x {c}m comprimento é de {area}m².')


l=float(input('Largura (m):'))
c=float(input('Comprimento (m):'))
calculo_area(l, c)