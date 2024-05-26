from random import randint
from time import sleep
mega = list()
print('_' * 40)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('_' * 40)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {n} JOGOS -=-=-=')
for c in range(1, n+1):
    jogo = [[randint(1, 60)], [randint(1, 60)], [randint(1, 60)], [randint(1, 60)], [randint(1, 60)],
            [randint(1, 60)], ]
    jogo.sort()
    mega.append(jogo[:])
    jogo.clear()
for cont, j in enumerate(mega):
    print(f'Jogo {cont+1}: {j} ')
    sleep(0.3)
print('{:-^40}'.format('< BOA SORTE >'))
