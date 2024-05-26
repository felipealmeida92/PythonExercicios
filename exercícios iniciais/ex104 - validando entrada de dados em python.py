def leiaInt(msg):
    """
    -> Função para ler um número inteiro válido
    :param msg: digitar um número inteiro
    :return: confirma se o número é inteiro e retorna em tela
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa Principal
num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')
