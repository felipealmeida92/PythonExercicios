n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
if n1 == n2:
    print('Não existe valor maior, {} e {} são iguais'.format(n1, n2))
elif n1 > n2:
    maior = n1
    print('O 1º valor {} é o maior'.format(n1))
else:
    maior = n2
    print('O 2º valor {} é o maior'.format(n2))

