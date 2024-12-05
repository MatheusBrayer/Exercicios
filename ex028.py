import random
import time
print('vou pensar em um numero de 0 a 5, tente adivinhar.')
num = random.randint(0,5) #gera um número aleatório

resp = int(input('Digite um numero entre 0 e 5:')) #usuário escolhe um número

print('Processando...')
time.sleep(2) #conta 2 segundos

if resp == num:
    print('ACERTOU, PARABÉNS VOCÊ VENCEU!')
else:
    print('VOCÊ ERROU! Eu pensei no numero {}'.format(num))