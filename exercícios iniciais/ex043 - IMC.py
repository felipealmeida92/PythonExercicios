peso = float(input('Digite seu pelo em (Kg) '))
altura = float(input('Digite sua altura em (m) '))
IMC = peso / (altura ** 2)
print('O seu IMC atual é {:.1f}'.format(IMC))
if IMC < 18.5:
    print('Você está abaixo do peso ideal')
elif (IMC >= 18.5) and (IMC < 25):
    print('Você está no peso ideal')
elif (IMC >= 25) and (IMC < 30):
    print('Você está com sobrepeso')
elif (IMC >= 30) and (IMC < 40):
    print('Você está com obesidade')
else:
    print('Você está em obesidade mórbida')
