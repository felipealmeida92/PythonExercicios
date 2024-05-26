from random import randint
computador = randint(1,10)
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
contvit = 0
while True:
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    soma = jogador + computador
    # Jogador Escolhe Par
    if escolha in 'P':
        if soma % 2 == 0:
            print('-' * 40)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu PAR')
            print('-' * 40)
            print('Você VENCEU!')
            contvit += 1
        else:
            print('-' * 40)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu ÍMPAR')
            print('-' * 40)
            print('Você PERDEU!')
            break
    # Jogador Escolhe Ímpar
    elif escolha in 'I':
        if soma % 2 == 0:
            print('-' * 40)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu PAR')
            print('-' * 40)
            print('Você PERDEU!')
            break
        elif soma % 2 == 1:
            print('-' * 40)
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} deu ÍMPAR')
            print('-' * 40)
            print('Você VENCEU!')
            contvit += 1
    else:
        print('Entrada Incorreta! Digite novamente')
print(f'GAME OVER! Você venceu {contvit} vezes.')
