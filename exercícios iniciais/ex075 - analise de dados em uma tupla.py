n = (int(input('Digite um valor inteiro: ')),
     int(input('Digite outro valor inteiro: ')),
     int(input('Digite mais um valor inteiro: ')),
     int(input('Digite o último valor inteiro: ')))
print(f'Você digitou os valores{n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
