num = int(input('Digite um número[999 para PARAR]: '))
soma = contd = 0
while True:
    if num == 999:
        break
    soma += num
    contd += 1
    num = int(input('Digite um número[999 para PARAR]: '))
print(f'Qtd valores informados: {contd} \nSoma: {soma}')
