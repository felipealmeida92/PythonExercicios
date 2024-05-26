sexo = str(input('Digite seu sexo [M/F] ')).upper().strip()
while sexo not in 'MnFf':
    sexo = str(input('Dados inválidos. Por favor, informe novamente: ')).upper().strip()
print('Sexo {} registrado com sucesso'.format(sexo))
