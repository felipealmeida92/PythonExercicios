from time import sleep
from random import randint


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'Somando os valores pares de {lista}, temos {s}')


# Programa Principal
numeros = list()
sorteia(numeros)
somaPar(numeros)