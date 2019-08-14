# Existem tres formas de iniciar uma variavel composta
# tupla = ()
# lista = []
# dicionario = {}
lanche = ('Hanburguer', 'Suco', 'Pizza', 'Pudin')
# Tambem posso escrever sem parenteses
# lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudin'
# O mesmo fatiamento pode ser feito de duas formas. Veja abaixo:
print('01:', lanche)
print('02:', lanche[0])
print('03:', lanche[-4])
print('04:', lanche[1])
print('05:', lanche[-3])
print('06:', lanche[2])
print('07:', lanche[-2])
print('08:', lanche[3])
print('09:', lanche[-1])
print('10:', lanche[1:3])
print('11:', lanche[-3:-1])
print('12:', lanche[1:])
print('13:', lanche[-3:])
print('14:', lanche[:2])
print('15:', lanche[:-2])
print(f'16: Qtd de lanches: {len(lanche)}')
# Tuplas sao imutaveis
# lanche[2] = 'Açai'
# print(lanche[2])
# E possivel usar a estrutura 'for' para ler Tuplas
for comida in lanche:
    print('17|', comida)
print('18: Acabaram os lanches!')
# Ou podemos usar o 'for' da maneira clasica
# com esse método eu pego a posicao
for contd in range(0, len(lanche)):
    print(f'19| Comida {contd}: {lanche[contd]}')
print('20: Geladeira vazia!')
# Uma outra forma de pegar a posicao e:
for pos, comida in enumerate(lanche):
    print(f'21| Comida {pos}: {comida}')
print('22: Dispensa vazia!')
# Mostrando intens de uma tupla de forma ordenada
# Quando isso é feito cria-se se uma LISTA com os itens ordenados
print('23:', sorted(lanche))
# Tuplas com numeros
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print('24:', a)
print('25:', b)
print('26:', c)
# quantas vezes um iten aparece
print('27:', c.count(5))
# Qual é a posicao de um iten
print('28:', c.index(8))
# Posicao de um item a partir de um determidado ponto
print('29:', c.index(2, 1))
# Tuplas aceitam diferentes tipos
pessoa = ('Marcos', 21, 1.74, 'M')
print('30:', pessoa)
# Apagando tupla da memoria
del(pessoa)
