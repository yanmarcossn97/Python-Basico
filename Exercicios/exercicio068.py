from random import randint
from time import sleep

contd = 0
while True:
    x = int(input('Escolha um número[0 a 5]: '))
    print()
    while x < 0 or x > 5:
        print('ERRO 97! Número inválido.')
        x = int(input('Escolha um número[0 a 5]: '))
        print()
    e = str(input('PAR ou IMPAR?[P]/[I] ')).strip().upper()[0]
    while e not in 'PI':
        print()
        print('ERRO 21! Dados inseridos inválidos.')
        e = str(input('Digite [P] para PAR ou [I] para IMPAR: ')).strip().upper()[0]
    y = randint(0, 5)
    soma = x + y
    if soma % 2 == 0:
        s = 'P'
        sort = 'PAR'
    else:
        s = 'I'
        sort = 'IMPAR'
    print()
    print(f'JOGADOR digitou {x} e esolheu a opção {e}')
    print(f'COMPUTADOR escolheu o número {y}')
    print(f'A SOMA desses números é {soma} que é {sort}')
    print('Analizando...')
    sleep(2)
    print()
    if e == s:
        print('JOGADOR ganhou!')
        contd += 1
    else:
        print('COMPUTADOR ganhou!')
        break
    sleep(2)
    print('Vamos jogar novamente...')
    print('.'*40)
    print()
print('Fim de jogo!')
print(f'Número de vitórias: {contd}')
