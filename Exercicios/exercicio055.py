print('O mais pesado e o mais leve em um grupo de 5')
maior = 0
menor = 0
# menor = 1000
# Na primeira vez que fiz utilizei a gabiarra acima.
# Mas depois aprendi a técnica do primeiro valor lido.
for c in range(1, 6):
    peso = float(input('Informe o peso da {}º pessoa(Kg): '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('Maior peso informado: {:.1f}Kg'.format(maior))
print('Menor peso informado: {:.1f}Kg'.format(menor))
