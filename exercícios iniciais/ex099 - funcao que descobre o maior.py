def maior(intervalo):
    from time import sleep
    maior = 0
    print('Analisando os valores passados...')
    for c in intervalo:
        if c > maior:
            maior = c
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(intervalo)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 30)


# início do programa
lista = [2, 9, 4, 5, 7, 1]
maior(lista)
lista1 = [4, 7, 0]
maior(lista1)
lista2 = [1, 2]
maior(lista2)
lista3 = [6]
maior(lista3)
lista4 = []
maior(lista4)