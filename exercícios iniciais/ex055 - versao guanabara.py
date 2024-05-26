maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('O peso da {}ª pessoa em (Kg): '.format(c)))
    if c ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
