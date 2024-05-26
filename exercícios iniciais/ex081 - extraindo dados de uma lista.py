valores = list()
while True:
    resp = ' '
    valores.append(int(input('Digite um valor: ')))
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista! na posição {valores.index(5)+1}')
else:
    print('O valor 5 não foi encontrado na lista!')
