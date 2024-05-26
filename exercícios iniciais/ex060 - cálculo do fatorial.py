from math import factorial
n1 = int(input('Digite um número para\ncalcular seu fatorial: '))
f = factorial(n1)
print('Calculando {}! ='.format(n1), end=' ')
while n1 != 0:
    print('{}'.format(n1), end='')
    print(' x ' if n1 > 1 else ' = ', end='')
    n1 += -1
print(f)


