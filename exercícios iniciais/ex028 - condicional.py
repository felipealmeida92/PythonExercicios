from random import randint
from time import sleep
aleatorio = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
escolha = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if escolha == aleatorio:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(aleatorio, escolha))
