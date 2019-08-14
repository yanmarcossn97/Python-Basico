from random import randint
from time import sleep

x = randint(0, 5)
print('Computador: "Pensei em um número entre 0 e 5. Advinha qual"...')
y = int(input('Você pensou no número: '))
print('Processando...')
sleep(3)
if y == x:
    print('Parabéns! Você acertou.')
else:
    print('Você errou! o número que eu pensei foi o {}.'.format(x))
