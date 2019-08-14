from random import randint
from time import sleep

print('ADVINHANDO NÚMERO')
print('-'*58)
n = randint(0, 10)
sleep(1)
print('MÁQUINA: Pensei em um número entre 0 e 10. Advinha qual...')
sleep(1)
x = int(input('JOGADOR: Você pensou no número: '))
print('MÁQUINA: Verificando...')
sleep(1)
print()
c = 1
if x != n:
    while x != n:
        if x < n:
            print('MÁQUINA: Não! Maior que {}'.format(x))
        elif x > n:
            print('MÁQUINA: Não! Menor que {}'.format(x))
        x = int(input('JOGADOR: Foi o número: '))
        print('MÁQUINA: Verificando...')
        sleep(1)
        c += 1
        print()
    print('-'*58)
    print('MÁQUINA: Parabéns! Você acertou.')
    print('MÁQUINA: Número de tentativas: {}'.format(c))
else:
    print('-'*58)
    print('MÁQUINA: Incrível! Você acertou de primeira.')
