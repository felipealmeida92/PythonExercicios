def leiaInt(msg):
    """
    -> Função para ler de um número inteiro válido
    :param msg: digitar um número inteiro
    :return: retorna um valor inteiro, ou erro caso não seja um número inteiro válido
    """
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário!\033[m')
            return 3
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1
    cabecalho('MENU PRINCIPAL')
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção... \033[m')
    return opc
