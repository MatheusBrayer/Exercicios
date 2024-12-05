# PROGRAMA QUE MOSTRA OS TIMES DO BRASILEIRÃO

times=('Inter','Gremio','Flamengo','São Paulo','Avai','Cruzeiro','Bota Fogo','Atlético PR','Atlético MG','Caxias',
       'Corinthias','Vasco','Cuiabá','Vitória','juventude','Criciuma','Fortaleza','Fluminese','Bragantino')
print(f'Lista de times do Brasileirão: {times}')
print('')
print(f'Lista dos 5 primeiros colocados: {times[0:5]}')
print('')
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('')
print(f'Times em ordem alfabética: {sorted(times)}')
print('')
print(f'O time {times[4]} está na {times.index("Avai")+1}° posição.')