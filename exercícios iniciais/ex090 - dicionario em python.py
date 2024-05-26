boletim = dict()
situacao = ' '
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input(f'Média de {boletim["nome"]}: '))
print('-=' * 30)
if boletim['media'] >= 7:
    boletim['situação'] = 'Aprovado'
elif 5 <= boletim['media'] < 7:
    boletim['situação'] = 'Recuperação'
else:
    boletim['situação'] = 'Reprovado'
for k, v in boletim.items():
    print(f'- {k} é igual a {v}')
