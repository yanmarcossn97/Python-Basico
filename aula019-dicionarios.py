# Criando um dicionario
# dados = {}
pessoa = dict()
pessoa = {'nome': 'Pedro', 'idade': 25}
print(f'00:', pessoa)
print(f'01:', pessoa['nome'])
print(f'02:', pessoa['idade'])

# Adicionando novos elementos a um dicionario
pessoa['sexo'] = 'M'
pessoa['peso'] = 75
pessoa['altura'] = 1.85
print(f'03:', pessoa)

# Alterando elementos de um dicionario
pessoa['nome'] = 'Marcos'
print(f'04:', pessoa)

# Deletando elementos
del pessoa['altura']
print(f'05:', pessoa)

# Mostrando valores, chaves e items
print(f'06:', pessoa.values())
print(f'07:', pessoa.keys())
print(f'08:', pessoa.items())

# Mostrando elementos de um dicionario com a estrutura 'for'
# Muito importante atençao aqui, pois temos um sintaxe diferente da usada nas listas
# for chave in pessoa.keys():
# for valor in pessoa.values():
for chave, valor in pessoa.items():
    print(f'09| {chave}: {valor}')

# Dicionarios dentro de listas
filme1 = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'George Lucas'}
filme2 = {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Josh Whedon'}
filme3 = {'titulo': 'Matriz', 'ano': 1999, 'diretor': 'Wachowski'}
locadora = []
locadora.append(filme1)
locadora.append(filme2)
locadora.append(filme3)
print(f'10:', locadora[0]['titulo'])
print(f'11:', locadora[1]['ano'])
print(f'12:', locadora[2]['diretor'])

# Inserindo elementos em um dicionario com a estrutura 'for'
# Outra diferenca em relaçao as listas. Para fazer uma copia usa-se o metodo 'exemplo.copy()' e nao (exemplo[:])
estado = dict()
brasil = list()
for i in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla: ')).strip().upper()
    brasil.append(estado.copy())
print(f'13:', brasil)

# Mostrando valores de um dicionario dentro de uma lista com a estrutura 'for'
for estado in brasil:
    for valores in estado.values():
        print(f'14| {valores}')
