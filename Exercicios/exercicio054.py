from datetime import date

aa = date.today().year
qtmen = 0
qtmai = 0
for c in range(1, 8):
    an = int(input('Insira o ano de nascim. da {}º pessoa: '.format(c)))
    id = aa - an
    if id < 21:
        qtmen += 1
    else:
        qtmai += 1
print('Qtd Menores(menos de 21): {}'.format(qtmen))
print('Qtd maiores(21 em diante): {}'.format(qtmai))
