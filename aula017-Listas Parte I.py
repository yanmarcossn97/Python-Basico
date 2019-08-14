# A lista é como uma tupla, mas com a diferença de que não é imutavel
# Criando lista vazia
compras = []
# ou dessa forma
compras = list()

# Criando lista ja com elementos
compras = ['Hamburguer', 'Suco', 'Pizza', 'Picolé']
print(f'Compras: {compras}')

# Fazendo uma copia de uma lista
alimentos = compras[:]
print(f'Alimentos(copia): {alimentos}')

# Alterando a copia, a original nao e alterada. e vice versa
# Adicionando um novo item em uma posicao especifica
alimentos.insert(0, 'Assaí')
print(f'Alimentos(copia): {alimentos}')
print(f'Compras(original): {compras}')

# Fazendo uma Ligaçao entre duas listas
lanche = compras
print(f'Lanches: {lanche}')

# Igualando duas listas, elas ficam ligadas. Alterando uma, a outra tambem altera
# Adicionando um novo item a uma lista(item é adicionado no final)
lanche.append('Biscoito')
print(f'Lanches alterada: {lanche}')
print(f'Compras tambem é alterada: {compras}')

# Alterando elemento em uma lista
lanche[2] = 'Pipoca'
print(lanche)

# Eliminando elemento pela chave usando comando
del lanche[1]
print(lanche)

# Eliminando elemento pela chave usando metodo '.pop()'(deixando sem a chave este metodo remove o ultimo item)
lanche.pop(3)
print(lanche)

# Eliminando elemento pelo conteudo usando metodo '.remove()'
lanche.remove('Picolé')
print(lanche)

# Posicao/chave/indice de elementos
for pos, elemento in enumerate(lanche):
    print(f'Chave {pos}: {elemento}')

# Verificado se um elemento existe em uma lista antes de remove-lo
if 'Hamburguer' in lanche:
    lanche.remove('Hamburguer')
else:
    print('O elemento "Hamburguer" não existe na lista LANCHE')

# Criando uma lista usando 'range()'
valores = list(range(4, 11))
print(valores)

# Criando uma lista pulando numeros
sequencia = list(range(3, 45, 5))
print(sequencia)

# Ordenando valores em uma lista
numeros = [4, 8, 1, 9, 7, 3]
print(numeros)
numeros.sort()
print(numeros)

# Ordenando valores reversamente
numeros.sort(reverse=True)
print(numeros)

# Verificando quantos elementos existem em uma lista
print(len(numeros))
