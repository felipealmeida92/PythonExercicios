n = int(input('Digite o 1º termo da PA '))
r = int(input('Digite a razão da PA '))
d = n + (10 - 1) * r
for c in range(n, d + r, r):
    print('{}'.format(c), end=' ')
