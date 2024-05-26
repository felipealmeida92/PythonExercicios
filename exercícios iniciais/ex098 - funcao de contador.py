def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    from time import sleep
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
            sleep(0.3)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            cont -= p
            sleep(0.3)
        print('FIM')

# início do programa
contador(0, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de persolanizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)