print('Valores ÍMPARES múltiplos de 3 entre 1 e 500')
soma = 0
contd = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        print(n)
        soma += n
        contd += 1
print('Soma desses valores: {}'.format(soma))
print('Qtd de valores: {}'.format(contd))
