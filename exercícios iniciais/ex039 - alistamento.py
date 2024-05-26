from datetime import date
nascimento = int(input('Digite o seu ano de nascimento '))
anoatual = date.today().year
idade = anoatual - nascimento
genero = str(input('Digite [F] se você é do sexo feminio e [M] se você é do sexo masculino ')).upper().strip()
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, anoatual))
if genero == 'M':
    if idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para seu alistamento!'.format(saldo))
        ano = anoatual + saldo
        print('Seu alistamento será em {}'.format(ano))
    elif idade == 18:
        print('Parabéns! Chegou a hora de se alistar no serviço militar'.format(idade))
    else:
        saldo = idade - 18
        print('Já passaram {} anos do prazo de alistamento'.format(saldo))
        ano = anoatual - saldo
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('Você não precisa se alistar no serviço militar!')