lista = list()
temp = list()
while True:
    media = 0
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Nota 1 ')))
    temp.append(float(input('Nota 2 ')))
    media = (media + temp[1] + temp[2])/2
    temp.append(media)
    lista.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 15)
print(f'{'Nº':<6}{'Nome':<11}{'Média':>8}')
print('-' * 30)
for p, l in enumerate(lista):
    print(f'{p:<5} {l[0]:<10} {l[3]:>8.2f}')
while True:
    print('-' * 30)
    opc = int(input('Quer mostrar a nota de qual aluno? (999 para interromper) '))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]} e {lista[opc][2]}')
    else:
        print('O valor não corresponde a um aluno cadastrado!')

