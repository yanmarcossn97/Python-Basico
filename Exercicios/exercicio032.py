from datetime import date

a = int(input('Informe um ano qualquer: '))
if a == 0:
    a = date.today().year
'''if a % 4 == 0:
    if a % 100 == 0:
        print('Esse ano tem 365 dias. Não é bissexto.')
    else:
        print('Esse ano tem 366 dias. É um ano bissexto.')
else:
    if a % 400 == 0:
        print('Esse ano tem 366 dias. É um ano bissexto.')
    else:
        print('Esse ano tem 365 dias. Não é um ano bissexto.')'''
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('{} é um ano bissexto.'.format(a))
else:
    print('{} não é um ano bissexto.'.format(a))
