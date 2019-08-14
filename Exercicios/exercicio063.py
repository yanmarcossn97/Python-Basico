print('SEQUÊNCIA DE FIBONACCI')
n = int(input('Quantos valores deseja obter? '))
i = 1
a = 1
b = 0
while i <= n:
    print('{}º: {}'.format(i, b))
    a = a + b
    b = a - b
    i += 1
print('Fim')
