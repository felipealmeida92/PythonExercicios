velocidade = float(input('Qual a velocidade do carro? Km/h '))
if velocidade > 80.00:
    multa = (velocidade - 80.00) * 7.00
    print('MULTADO! você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Sua velocidade foi {}Km/h. Você está dentro do limite de velocidade de 80Km/h'.format(velocidade))
