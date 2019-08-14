v = float(input('Velocidade do carro (Km/h): '))
if v > 80:
    print('Você ultrapassou o limite de velocidade!')
    print('O limite é de 80Km/h.')
    print('Valor da multa: {:.2f} R$'.format((v-80)*7))
else:
    print('Dentro do limite de velocidade.')
