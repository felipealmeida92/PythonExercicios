from random import randint
from time import sleep
tentativas = 0
computador = randint(1, 10)
n = 0
print('\033[1;32m-=' * 30)
print('Vou pensar em um número entre [1 e 10], tente adivinhar...')
print('-=' * 30, '\033[m')
while n != computador:
    n = int(input('Em que número eu pensei? '))
    print('\033[31mPROCESSANDO...\033[m')
    sleep(0.3)
    if n != computador:
        tentativas += 1
        if n < computador:
            print('Mais! Você ERROU!, tente novamente')
        else:
            print('Menos! Você ERROU!, tente novamente')
print('PARABÉNS! Você acertou')
print('Foram necessárias {} tentativas para acertar'.format(tentativas+1))
