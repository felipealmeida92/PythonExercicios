s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('O somatório entre os {} números múltiplos de 3 no intervalo é {}'.format(cont, s))
