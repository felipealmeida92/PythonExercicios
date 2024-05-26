numero = int(input('Digite um número inteiro qualquer '))
print('\033[1;34m[1]\033[m \033[0;97mpara\033[m \033[0;35mbinário\033[m')
print('\033[1;34m[2]\033[m \033[0;97mpara\033[m \033[0;35moctal\033[m')
print('\033[1;34m[3]\033[m \033[0;97mpara\033[m \033[0;35mhexadecimal\033[m')
base = int(input('Em qual base de conversão você deseja? '))
if base == 1:
    print('Você escolheu binário e o resultado será {}'.format(bin(numero)[2:]))
elif base == 2:
    print('Você escolheu octal e o resultado será {}'.format(oct(numero)[2:]))
elif base == 3:
    print('Você escolheu hexadecimal e o resultado será {}'.format(hex(numero)[2:]))
else:
    print('Opação inválida! Tente novamente')