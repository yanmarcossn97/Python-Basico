'''for c in range(1, 10):
    print(c)
print('Fim')'''
# c = 1
'''while c < 10:
    print(c)
    c += 1
print('Fim')'''
'''while c != 0:
    c = int(input('Digite um número: '))
print('Fim')'''
# r = 'S'
'''while r == 'S':
    c = int(input('Digite um número: '))
    r = str(input('Quer continuar?[S]/[N]: ')).upper()
    print()
print('Fim')'''

n = 1
qtpares = qtimpares = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            qtpares += 1
        else:
            qtimpares += 1
print('Qtd PARES: {}; Qtd IMPARES: {}'.format(qtpares, qtimpares))
