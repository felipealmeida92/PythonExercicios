salario = float(input('Qual o salário do funcionário? R$: '))
if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario, aumento))
