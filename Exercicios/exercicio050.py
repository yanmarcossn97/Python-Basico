soma = 0
for c in range(0, 6):
    n = int(input('Digite um número qualquer: '))
    if n % 2 == 1:
        soma += n
print('Soma dos ÍMPARES: {}'.format(soma))
