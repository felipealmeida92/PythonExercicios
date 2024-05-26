print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Digite o primeiro lado do triângulo '))
r2 = float(input('Digite o segundo lado do triângulo '))
r3 = float(input('Digite o terceiro lado do triângulo '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')