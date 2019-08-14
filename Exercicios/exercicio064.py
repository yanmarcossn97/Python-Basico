contd = soma = num = 0
while num != 999:
    num = int(input('Digite um número [999 para PARAR]: '))
    if num != 999:
        contd += 1
        soma += num
print('Qtd números informados: {}'.format(contd))
print('Soma dos valores informados: {}'.format(soma))
