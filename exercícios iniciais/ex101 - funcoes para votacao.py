def voto(ano=0):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print(f'Com {idade}:', end=' ')
    if idade < 16:
        print('NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        print('VOTO OPCIONAL.')
    else:
        print('VOTO OBRIGATÓRIO.')


# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
