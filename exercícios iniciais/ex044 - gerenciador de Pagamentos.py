preço = float(input('Digite o valor do produto '))
print('=' * 45)
print('{:=^45}'.format(' Lojas Flypekiller '))
print('\033[1mTABELA DE DESCONTOS\033[m')
print('\033[0;30;47m[1] PAGAMENTO DINHEIRO/CHEQUE: 10% DESCONTO\033[m')
print('\033[0;30;47m[2] PAGAMENTO À VISTA CARTÃO: 5% DESCONTO\033[m')
print('\033[0;30;47m[3] PAGAMENTO EM 2X NO CARTÃO: PREÇO NORMAL\033[m')
print('\033[0;30;47m[4] PAGAMENTO EM 3X OU MAIS NO CARTÃO: 20% JUROS\033[m')
print('=' * 45)
escolha = int(input('Escolha a forma de pagamento: '))
print('Você escolheu a opção [{}] '.format(escolha))
if escolha == 1:
    print('O valor do produto é {:.2f} e você pagará {:.2f} que corresponde a 10% de desconto'.format(preço, preço * 0.90))
elif escolha == 2:
    print('O valor do produto é {:.2f} e você pagará {:.2f} que corresponde a 5% de desconto'.format(preço, preço * 0.95))
elif escolha == 3:
    print('O valor de cada parcela será R${:.2f}'.format(preço / 2))
    print('O valor do produto não terá desconto e você pagará R${:.2f}'.format(preço))
elif escolha == 4:
    parcelas = int(input('Digite o número de parcelas '))
    print('O valor de cada parcela será R${:.2f}'.format(preço / parcelas))
    print('O valor do produto é {:.2f} e você pagará {:.2f} que corresponde a 20% de juros'.format(preço, preço * 1.20))
else:
    print('Escolha inválida!')