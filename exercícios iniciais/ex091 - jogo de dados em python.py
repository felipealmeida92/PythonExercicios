from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
dados = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('-=' * 30)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print(' == Ranking dos jogadores: == ')
for k, v in enumerate(ranking):
    print(f'  {k+1}º lugar: {v[0]} com {v[1]}. ')
    sleep(1)