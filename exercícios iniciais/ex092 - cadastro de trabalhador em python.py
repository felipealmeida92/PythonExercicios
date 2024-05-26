from datetime import date
ficha = dict()
ficha['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
ficha['idade'] = date.today().year - ano
ficha['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['contratacao'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: R$ '))
    ficha['aposentadoria'] = (ficha['contratacao'] + 35) - ano
print('-=' * 30)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}')