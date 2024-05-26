valor = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for p in range(0, 3):
    for c in range(0, 3):
        valor[p][c] = int(input(f'Digite um valor para [{p}, {c}] '))
print('-=' * 30)
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[{valor[p][c]:^5}]', end='')
    print()
