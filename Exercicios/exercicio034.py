s = float(input('Valor atual do salário: '))
if s > 1250:
    print('Novo salário com aumento: {:.2f} R$'.format(s*1.1))
else:
    print('Novo salário com aumento: {:.2f} R$'.format(s*1.15))
