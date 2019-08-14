from random import randint
numero1 = randint(0, 99)
numero2 = randint(0, 99)
numero3 = randint(0, 99)
numero4 = randint(0, 99)
numero5 = randint(0, 99)
valores = (numero1, numero2, numero3, numero4, numero5)
print('Números informados: ', end='')
for chave, numero in enumerate(valores):
    print(numero, end=', ')
    if chave == 0:
        menor = maior = numero
    elif numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero
print(f'\nMenor número: {menor}')
print(f'Maior número: {maior}')
