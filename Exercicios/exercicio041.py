from datetime import date

an = int(input('Ano de nascimento: '))
aa = date.today().year
i = aa - an
print('Idade: {} anos.'.format(i))
if 7 <= i <= 9:
    print('Categoria: Mirin.')
elif 9 < i <= 14:
    print('Categoria: Infantil.')
elif 14 < i <= 19:
    print('Categoria: Júnior.')
elif 19 < i <= 20:
    print('Categoria: Sênior.')
elif 20 < i <= 40:
    print('Categoria: Master.')
else:
    print('Categoria: Nenhuma.')
