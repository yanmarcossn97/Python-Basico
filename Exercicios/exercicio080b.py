# Inserindo valores em uma lista já em ordem
valores = []
for contd in range(0, 7):
    numero = int(input(f'{contd + 1}º Valor: '))
    if contd == 0:
        valores.append(numero)
    elif numero <= valores[0]:
        valores.insert(0, numero)
    elif numero > valores[contd - 1]:
        valores.append(numero)
    else:
        for c in range(1, contd):
            if numero <= valores[c]:
                valores.insert(c, numero)
                break
print(f'Valores em ordem: {valores}')
