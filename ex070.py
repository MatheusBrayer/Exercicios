# ESTATISTICAS EM PRODUTOS
preço_total=mais_barato=contador=mais_de_mil=produto_mais_barato=0
while True:
    produto=str(input('Nome do produto: ')).strip()
    preço=float(input('Preço: R$'))
    preço_total+=preço
    contador+=1
    if contador<=1:
        mais_barato=preço
    else:
        if preço<mais_barato:
            mais_barato=preço
            produto_mais_barato=produto
    if preço>1000:
        mais_de_mil+=1
    continuar = str(input('Deseja continuar?')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?')).upper().strip()[0]
    if continuar=='N':
        break
print(f'O valor total da compra foi de R${preço_total:.2f}.')
print(f'Temos {mais_de_mil} produto com valor superior a R$1000,00.')
print(f'O produto mais barato foi {produto_mais_barato} que custa R${mais_barato:.2f}')