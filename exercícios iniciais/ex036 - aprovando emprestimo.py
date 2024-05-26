valor = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o salário? R$ '))
tempo = int(input('Quantos anos irá pagar? '))
parcela = valor / (tempo * 12)
print('O valor da parcela será R${:.2f}'.format(parcela))
if parcela > (salario * 0.30):
    print('Seu empréstimo foi negado porque o valor da parcela R${:.2f} é superior a 30% do salário R${:.2f}'.format(parcela, salario))
else:
    print('Empréstimo aprovado!')