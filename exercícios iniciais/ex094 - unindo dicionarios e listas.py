pessoas = dict()
grupo = list()
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    grupo.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f' A) O grupo tem {len(grupo)} pessoas.')
media = soma / len(grupo)
print(f' B) A média de idade é de {media:.2f} anos')
print(' C) As mulheres cadastradas foram: ', end='')
for k in grupo:
    if k["sexo"] == 'F':
        print(k["nome"], end=' ')
print()
print(' D) Lista das pessoas que estão acima da média: ')
for k in grupo:
    if k["idade"] >= media:
        for n, p in k.items():
            print(f'{n} = {p}', end='; ')
        print()
print('<< ENCERRADO >>')
