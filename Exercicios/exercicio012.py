p = float(input('Preço atual do produto(BR$): '))
t = int(input('Taxa de desconto da promoção(%): '))
print('Com desconto sai por: {:.2f} R$'.format(p*(1-t/100)))
