m = float(input('Digite o seu peso(Kg): '))
h = float(input('digite a sua altura(m): '))
imc = m / h**2
print('Seu IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('você está ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('você está no PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA.')
