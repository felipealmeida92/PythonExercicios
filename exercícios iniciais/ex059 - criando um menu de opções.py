from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
maior = n1
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>> Qual é a opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 == n2:
            print('Não há maior entre {} e {} eles são iguais'.format(n1, n2))
        if n1 < n2:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        else:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Digite os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-'*20)
    sleep(1)
