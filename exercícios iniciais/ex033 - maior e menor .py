a = int(input('Digite o primeiro número inteiro '))
b = int(input('Digite o segundo número inteiro '))
c = int(input('Digite o terceiro número inteiro '))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {} e o maior valor digitado foi {}'.format(menor, maior))
