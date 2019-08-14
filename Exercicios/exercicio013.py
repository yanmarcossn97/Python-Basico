s = float(input('Sálario atual(BR$): '))
p = int(input('Porcentagem de aumento(%): '))
print('Novo salário com aumento: {:.2f} R$.'.format(s*(1+p/100)))
