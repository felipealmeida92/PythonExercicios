from bisect import insort
valores = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    insort(valores, n)
    print(f'Número {n} inserido na posição {valores.index(n)}')
    print(f'Lista atualizada {valores}')