from random import randint
from time import sleep
serie = list()
mega = list()
print('-' * 30)
print('       JOGA NA MEGA SENA       ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in serie:
            serie.append(n)
            cont += 1
        if cont >= 6:
            break
    serie.sort()
    mega.append(serie[:])
    serie.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, j in enumerate(mega):
    print(f'Jogo {i+1}: {j}')
    sleep(0.5)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
