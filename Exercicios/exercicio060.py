print('FATORIAL DE UM NÚMERO')
n = int(input('Fatorial de: '))
f = 1
expr = ''
print('{}! = '.format(n), end='')
while n > 0:
    # f = f * n
    f *= n
    expr = expr + '{} x '.format(n)
    # n = n - 1
    n -= 1
tm = len(expr) - 2
print(expr[:tm], end='')
print('= {}'.format(f))

# print('{}'.format(n), end='')
# print(' x ' if n > 1 else ' = ', end='')
