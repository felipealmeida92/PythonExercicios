n = int(input('Qual tabuada quer resolver? '))
for c in range(1, 11):
    print('{: ^1} x {: ^2} = {: ^4}'.format(n, c, n * c))

