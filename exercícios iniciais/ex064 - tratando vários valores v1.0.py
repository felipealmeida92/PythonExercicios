parada = 999
n = s = c = 0
print('\033[1;31mPara encerrar digite [999]\033[m')
while n != parada:
    n = int(input('Digite um número '))
    if n != parada:
        s += n
        c += 1
        print('Digite outro valor')
print('Você digitou {} números e a soma dos valores digitados foi {}'.format(c, s))
