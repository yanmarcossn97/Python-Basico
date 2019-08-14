tabuada = int(input('Tabuada do [0 para PARAR]: '))
while True:
    if tabuada == 0:
        break
    contd = 0
    while contd <= 10:
        print(f'{tabuada} x {contd:2} = {tabuada * contd}')
        contd += 1
    print()
    tabuada = int(input('Tabuada do[0 para PARAR]: '))
print('Fim')
