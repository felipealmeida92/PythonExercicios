frase = str(input('Digite uma frase qualquer ')).upper().strip()
dividido = frase.split()
junto = ''.join(dividido)
inverso = ''
# inverso = junto[::-1] (opção sem o for)
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')