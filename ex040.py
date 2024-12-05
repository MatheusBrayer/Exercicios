# Exercico de média de notas escolares

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print('Tirando {} e {}, tem a média {}'.format(n1, n2, m))

if m >= 7:
    print('\033[32m O aluno está APROVADO!\033[m')

elif m > 5 and m < 7:
    print('\033[33m O aluno está em RECUPERAÇÃO!\033[m')

elif m < 7:
    print('\033[31m O aluno foi REPROVADO!\033[m')

