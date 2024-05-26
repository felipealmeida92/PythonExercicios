matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = s3 = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
    print()
for l in range(0, 3):
    s3 += matriz[l][2]
for c in range(0, 3):
    mai = max(matriz[1])
print('-=' * 30)
print(f'A soma dos valores pares é {s}')
print(f'A soma dos valores da terceira coluna é {s3}')
print(f'O maior valor da segunda linha é {mai}')
