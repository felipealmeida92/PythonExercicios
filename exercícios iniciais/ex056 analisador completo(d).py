s = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M]')).strip()
    s += idade
    m = (s / 4)
    if c == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        totmulher20 += 1
print('A média de idades do grupo é {}'.format(m))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print(f'A quantidade de mulheres menores de 20 anos é {totmulher20}')
