valor = contd = 0
numeros = []
qtval = int(input('Quantos valores: '))
while True:
    while contd < qtval:
        contd += 1
        valor = int(input(f'{contd}º valor: '))
        if valor in numeros:
            print('VALOR REPETIDO. NÃO SERÁ ADICIONADO!')
        else:
            numeros.append(valor)
    ad = int(input('\nMais quantos valores: '))
    if ad > 0:
        qtval += ad
    else:
        break
print('\nPROCESSO FINALIZADO')
print(f'Valores inseridos: {sorted(numeros)}')
