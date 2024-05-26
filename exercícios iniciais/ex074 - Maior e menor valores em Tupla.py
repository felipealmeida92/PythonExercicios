from random import randint
aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10),
             randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for c in aleatorio:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi {max(aleatorio)}')
print(f'O menor valor sorteado foi {min(aleatorio)}')