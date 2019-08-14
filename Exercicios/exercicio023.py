valor = int(input('Digite um número entre 0 e 9999: '))
# num = str(valor)
# print('Unidades: {}.'.format(num[3]))
# print('Dezenas: {}.'.format(num[2]))
# print('Centenas: {}.'.format(num[1]))
# print('Unid. de milhar: {}.'.format(num[0]))
u = valor // 1 % 10
d = valor // 10 % 10
c = valor // 100 % 10
um = valor // 1000 % 10
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centenas: {}'.format(c))
print('Unid. de milhar: {}'.format(um))
