from datetime import date

an = int(input('Ano de nascimento: '))
aa = date.today().year
i = aa - an
if i == 18:
    print('Você completa 18 anos este ano.')
    print('Está na idade para fazer o alistamento militar.')
elif i < 18:
    print('Idade: {} anos.'.format(i))
    print('Ainda não está na idade para o alistamento militar.')
    print('Faltam {} anos.'.format(18 - i))
    print('Seu alistamento será em {}.'.format(aa + 18 - i))
else:
    print('Idade: {}'.format(i))
    print('Você passou da idade para o alistamento militar.')
    print('Atraso: {} anos.'.format(i - 18))
    print('Seu alistamento deveria ter sido em {}.'.format(aa - (i - 18)))
