n = int(input('Digite um número inteiro qualquer '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        tot += 1
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi pode ser dividido {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
