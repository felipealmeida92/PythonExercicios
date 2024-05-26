partida = dict()
gols = list()
partida['nome'] = str(input('Nome: '))
quant = int(input(f'Quantas partidas {partida['nome']} jogou? '))
for c in range(1, quant+1):
    n = int(input(f'Quantos gols na partida {c}? '))
    gols.append(n)
partida['gols'] = gols[:]
partida['total'] = sum(gols)
print('-=' * 30)
print(partida)
print('-=' * 30)
for k, v in partida.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {partida['nome']} jogou {quant} partidas.')
for x, y in enumerate(partida['gols']):
    print(f'    => Na partida {x+1}, fez {y} gols.')
print(f'Foi um total de {partida['total']} gols.')
