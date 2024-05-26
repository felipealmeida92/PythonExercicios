valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {valores}')
for c, p in enumerate(valores):
    if p % 2 == 0:
        par.append(p)
    else:
        impar.append(p)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
