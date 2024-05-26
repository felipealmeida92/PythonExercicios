pessoas = list()
dados = list()
pesado = leve = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append((float(input('Peso: '))))
    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {pesado}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == pesado:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi {leve}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == leve:
        print(f'[{p[0]}]', end=' ')
print()
