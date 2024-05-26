banco = 'BANCO CEV'
print('=' * 40)
print(f'{banco:^40}')
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totalced = 0
# considerar cédulas de R$50,00 - R$20,00 - R$10,00 - R$1,00
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'O total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre ao BANCO CV! Tenha um bom dia!')


