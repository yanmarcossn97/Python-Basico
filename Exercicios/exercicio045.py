from random import randint

print('[1] Pedra [2] Papel [3] Tesoura.')
print('-'*35)
x = int(input(('VEZ JOGADOR. Escolha um opção: ')))
if x == 1:
    print('Jogador escolheu PEDRA')
elif x == 2:
    print('Jogador escolheu PAPEL')
elif x == 3:
    print('Jogador escolheu TESOURA')
print('VEZ MÁQUINA')
y = randint(1, 3)
if y == 1:
    print('Máquina escolheu PEDRA')
elif y == 2:
    print('Máquina escolheu PAPEL')
elif y == 3:
    print('Máquina escolheu TESOURA')
print('-'*35)
if x == 1 and y == 1 or x == 2 and y == 2 or x == 3 and y == 3:
    print('EMPATE. Ambos escolheram a mesma opção.')
elif x == 1 and y == 2 or x == 2 and y == 3 or x == 3 and y == 1:
    print('MÁQUINA venceu!')
elif x == 1 and y == 3 or x == 2 and y == 1 or x == 3 and y == 2:
    print('JOGADOR venceu!')
