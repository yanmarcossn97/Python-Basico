num = soma = 0
while True:
    num = int(input('Digite um número[999 para PARAR]: '))
    if num == 999:
        break
    soma += num
# print('Soma: {}'.format(soma))
# O comando print acima pode ser feita da forma abaixo: isso se chama 'f' string
print(f'Soma: {soma}')
