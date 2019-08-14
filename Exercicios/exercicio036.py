from time import sleep

print('VERIFICAÇÃO DE CRÉDITO P/ FINANCIAMENTO DE CASA.')
print('*'*50)
print('*'*50)
x = float(input('Valor da casa(R$): '))
y = float(input('Renda mensal do comprador(R$): '))
z = int(input('Qtd meses/parcelas do financiamento: '))
print('Fazendo análise...')
ValParc = x / z
ValMaxParc = y * 0.3
QtdMinParc = x / ValMaxParc
sleep(3)
print('*'*50)
print('SITUAÇÃO:')
if ValParc <= ValMaxParc:
    print('CRÉDITO APROVADO! \nO valor da parcela ficou DENTRO do limite.')
else:
    print('CRÉDITO NEGADO! \nO valor da parcela ficou ACIMA do limite.')
    print("Qtd mín. de parcelas para ser aprovado: {:.0f}".format(QtdMinParc))
print('*'*50)
print('DADOS DA ANÁLISE:')
print('Valor da parcela: {:.2f} R$'.format(ValParc))
print('Limite(30% da renda): {:.2f} R$'.format(ValMaxParc))
