dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
custo = (dias * 60.00) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(custo))
