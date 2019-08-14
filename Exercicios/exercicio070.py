from time import sleep
codigo = total = caros = maiscaro = qtprod = barato = 0
prodcaro = prodbarato = ''
print('{:-^50}'.format(' LISTA DE COMPRAS '))
print()
while True:
    codigo += 1
    qtprod += 1
    print('Produto {:2} {:->39}'.format(codigo, ''))
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço(BR$): '))
    total += preco
    if codigo == 1 or preco < barato:
        barato = preco
        prodbarato = nome
    if preco > 1000:
        caros += 1
    if preco > maiscaro:
        maiscaro = preco
        prodcaro = nome
    print()
    cond = ' '
    while cond not in 'SN':
        cond = str(input('ADICIONAR MAIS PRODUTOS?[S]/[N] ')).strip().upper()[0]
    print()
    if cond == 'N':
        break
print('LISTA FINALIZADA! GERANDO NOTA...')
sleep(2)
print()
print('{:-<50}'.format('NOTA '))
print('Total a pagar: {:>32.2f} R$'.format(total))
print('Qtd de produtos: {:>25} prod(s)'.format(qtprod))
print('Acima de 1000 R$: {:>24} prod(s)'.format(caros))
print('Mais caro: {:>27} {:8.2f} R$'.format(prodcaro,  maiscaro))
print('Mais barato: {:>25} {:8.2f} R$'.format(prodbarato, barato))
