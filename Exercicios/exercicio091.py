from random import randint
from time import sleep
pessoa = {}
partida = []
nome = lado = ''
for c in range(1, 6):
    pessoa['nome'] = f'Jogador{c}'
    pessoa['lado'] = randint(1, 6)
    partida.append(pessoa.copy())
print('JOGANDO DADOS...')
for pessoa in partida:
    sleep(1)
    print('{} saiu o lado {}'.format(pessoa['nome'], pessoa['lado']))
for c in range(0, 4):
    for i in range((c + 1), 5):
        if partida[c]['lado'] < partida[i]['lado']:
            nome = partida[c]['nome']
            lado = partida[c]['lado']
            partida[c]['nome'] = partida[i]['nome']
            partida[c]['lado'] = partida[i]['lado']
            partida[i]['nome'] = nome
            partida[i]['lado'] = lado
print('\nRANQUING...')
for pos, pessoa in enumerate(partida):
    sleep(1)
    print('{}º Posição: {} com {} pts'.format(pos + 1, pessoa['nome'], pessoa['lado']))
