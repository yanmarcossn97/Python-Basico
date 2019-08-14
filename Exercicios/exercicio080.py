# Inseridos 5 valores em uma lista já na posiçao certa
valores = []
contd = 0
num = int(input('Informe um número: '))
valores.append(num)
num = int(input('Informe um numero: '))
contd += 1
if num <= valores[0]:
    valores.insert(0, num)
else:
    valores.append(num)
num = int(input('Informe um numero: '))
contd += 1
if num <= valores[0]:
    valores.insert(0, num)
else:
    if num <= valores[(contd - 1)]:
        valores.insert(contd - 1, num)
    else:
        valores.append(num)
num = int(input('informe um numero: '))
contd += 1
if num <= valores[0]:
    valores.insert(0, num)
else:
    if num <= valores[contd - 2]:
        valores.insert(contd - 2, num)
    else:
        if num <= valores[contd - 1]:
            valores.insert(contd - 1, num)
        else:
            valores.append(num)
num = int(input('Digite um número: '))
contd += 1
if num <= valores[0]:
    valores.insert(0, num)
else:
    if num <= valores[contd - 3]:
        valores.insert(contd - 3, num)
    else:
        if num <= valores[contd - 2]:
            valores.insert(contd - 2, num)
        else:
            if num <= valores[contd - 1]:
                valores.insert(contd - 1, num)
            else:
                valores.append(num)
print(f'Valores em ordem: {valores}')
