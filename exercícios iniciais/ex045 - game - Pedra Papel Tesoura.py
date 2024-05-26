from random import choice
from time import sleep
lista = ['✊', '✋', '✌️']
bot = choice(lista)
print('xXx' * 12)
print('\033[1mJOGO DO ✊PEDRA, ✋PAPEL E ️✌️TESOURA\033[m')
print('xXx' * 12)
print('[1] para ✊ (Pedra)')
print('[2] para ✋ (Papel)')
print('[3] para ✌️ (Tesoura)')
print('xXx' * 12)
escolha = int(input('Escolha sua jogada '))
print('Pedra...')
sleep(0.5)
print('Papel...')
sleep(0.5)
print('Tesoura!')
sleep(0.5)
print('xXx' * 12)
if (bot == '✊' and escolha == 2) or (bot == '✋' and escolha == 3) or (bot == '✌️' and escolha == 1):
    print('Computador escolheu {}! Jogador venceu!'.format(bot))
    if escolha == 1:
        nome = '✊'
    elif escolha == 2:
        nome = '✋'
    elif escolha == 3:
        nome = '✌️'
    print('O jogador escolheu {}'.format(nome))
elif (bot == '✊' and escolha == 1) or (bot == '✋' and escolha == 2) or (bot == '✌️' and escolha == 3):
    print('Computador escolheu {}! Empate'.format(bot))
    if escolha == 1:
        nome = '✊'
    elif escolha == 2:
        nome = '✋'
    elif escolha == 3:
        nome = '✌️'
    print('O jogador escolheu {}'.format(nome))
elif (bot == '✊' and escolha == 3) or (bot == '✋' and escolha == 1) or (bot == '✌️' and escolha == 2):
    print('Computador escolheu {}! Jogador perdeu!'.format(bot))
    if escolha == 1:
        nome = '✊'
    elif escolha == 2:
        nome = '✋'
    elif escolha == 3:
        nome = '✌️'
    print('O jogador escolheu {}'.format(nome))
else:
    print('O valor escolhido é inválido!')
