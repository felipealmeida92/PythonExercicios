def area(x, y):
    a = x * y
    print(f'A área de um terreno de {x}x{y} é de {a}m².')


def título(txt):
    print(txt)
    print('-' * len(txt))


# inicio
título('Controle de Terrenos')
p = float(input('LARGURA (m): '))
q = float(input('COMPRIMENTO (m): '))
area(p, q)
