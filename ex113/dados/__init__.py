def leiaInt(msg):
    """
    -> Função para ler um número inteiro válido
    :param msg: digitar um número inteiro
    :return: retorna um erro caso não seja inteiro, retorna o valor digitado caso seja inteiro
    """
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    """
    -> Função para ler um número real válido
    :param msg: digitar um número real
    :return: retorna uma mensagem de erro caso não seja um valor real, retorna o valor digitado caso seja real
    """
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 0
        else:
            return n
