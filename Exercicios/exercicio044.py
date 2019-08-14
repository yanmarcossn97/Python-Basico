print('{:*^40}'.format(' CARRINHO DE COMPRAS '))
preco = float(input('Valor no carrinho(BRS): '))
print('*'*40)
print('FORMA DE PAGAMENTO')
print('[0] À vista: 10% de desconto')
print('[1] À vista no cartão: 5% de desconto')
print('[2] 2x no cartão: preço normal')
print('[3 a 12] 3x a 12x no cartão: 20% de juros')
print('*'*40)
parc = int(input('Escolha a forma de pagamento: '))
if parc == 0:
    valor = preco * 0.9
    status = 'Compra aprovada'
elif parc == 1:
    valor = preco * 0.95
    status = 'Compra aprovada'
elif parc == 2:
    valor = preco
    valparc = valor / parc
    status = 'Compra aprovada'
    print('Parcelamento: 2X de {:.2f} R$'.format(valparc))
elif 3 <= parc <= 12:
    valor = preco * 1.2
    valparc = valor / parc
    status = 'Compra aprovada'
    print('Parcelamento: {}x de {:.2f} R$'.format(parc, valparc))
else:
    valor = 0
    status = 'Compra cancelada'
    print('ERRO! Opção de pagamento inválida.')
print('VALOR FINAL DA COMPRA: {:.2f} R$'.format(valor))
print('STATUS: {}.'.format(status))
