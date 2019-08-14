print('Progressão Aritimética(PA)')
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
print('10 primeiros termos:')
for c in range(1, 11):
    print('{:2}º termo: {}'.format(c, n))
    n += r
print('Fim')
