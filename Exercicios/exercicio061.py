n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
print('10 primeiros termos da PA: ', end='')
while c < 10:
    print(n1, end=', ')
    n1 += r
    c += 1
print('Fim')
