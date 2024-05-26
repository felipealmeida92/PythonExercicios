from datetime import date
nascimento = int(input('Digite seu ano de nascimento '))
atual = date.today().year
idade = (atual - nascimento)
if idade <= 9:
    print('Você tem {} anos e está na categoria: MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e está na categoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e está na categoria: JUNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e está na categoria: SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e está na categoria: MASTER'.format(idade))
