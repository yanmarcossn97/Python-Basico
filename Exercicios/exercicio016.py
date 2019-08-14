import math

# math.floor(x) - arredonda x para baixo
# math.ceil(x) - arredonda x para cima
# math.fabs(x) - retorna valor absoluto de x
# math.factorial(x) - calcula o fatorial de x
n = float(input('Digite um número: '))
print('Arredondamento para baixo: {}.'.format(math.floor(n)))
print('Arrendondamento para cima: {}.'.format(math.ceil(n)))
print('valor absoluto: {}.'.format(math.fabs(n)))
print('Fatorial: {}.'.format(math.factorial(n)))
