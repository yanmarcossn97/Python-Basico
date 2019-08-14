d = float(input('Insira a distância da viagem(Km): '))
if d <= 200:
    print('Custo da viagem: {:.2f} R$'.format(d*0.5))
else:
    print('Custo da viagem: {:.2f} R$'.format(d*0.45))
