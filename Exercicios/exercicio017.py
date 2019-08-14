import math

# math.hypot(x, y) - calcula a hip de um triang retang de catetos x e y
x = float(input('Insira o cateto oposto(cm): '))
y = float(input('Insira o cateto adacente(cm): '))
h = (x**2 + y**2)**(1/2)
# print('Hipotenusa: {}.'.format(h))
print('Hipotenusa: {}.'.format(math.hypot(x, y)))
