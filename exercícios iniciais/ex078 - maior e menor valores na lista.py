valores = list()
posicao_maior = list()
posicao_menor = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-' * 40)
for i, j in enumerate(valores):
    if j == max(valores):
        posicao_maior.append(i)
    if j == min(valores):
        posicao_menor.append(i)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições {posicao_maior}')
print(f'O menor valor digitado foi {min(valores)} nas posições {posicao_menor}')
