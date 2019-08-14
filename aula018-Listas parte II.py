# Copiando listas para dentro de outras listas
dados1 = []
dados1.append('Pedro')
dados1.append(25)
print(f'01:', dados1)

dados2 = []
dados2.append('Maria')
dados2.append(19)
print(f'02:', dados2)

dados3 = []
dados3.append('João')
dados3.append(32)
print(f'03:', dados3)

pessoas = []
pessoas.append(dados1[:])
pessoas.append(dados2[:])
pessoas.append(dados3[:])
print(f'04:', pessoas)

# Isso tambem pode ser feito diretamente na criaçao da lista
pessoas2 = [['Ana', 19], ['Eva', 21], ['Diana', 20]]
print(f'05:', pessoas2)

# Mostrando os elementos com a estrutura 'for'
for p in pessoas2:
    print(f'06| {p[0]} {p[1]};')

# Acessando elementos específicos
print(f'07:', pessoas[0][0])
print(f'09:', pessoas2[1][1])
print(f'09:', pessoas[2][0])

# Acessando uma lista interna
print(f'10:', pessoas[1])
print(f'11:', pessoas[2])

# Alterando elementos em uma lista interna
test = list()
test.append('Natália')
test.append(34)
grupo = list()
grupo.append(test)
print(f'12:', grupo)
test[0] = 'Luana'
test[1] = 45
print(f'13:', grupo)

# Adicionando mais elementos em uma lista interna(fazendo copia dos dados)
test1 = list()
test1.append('Marcos')
test1.append(21)
grupo1 = list()
grupo1.append(test1[:])
print(f'14:', grupo1)
test1[0] = 'Karol'
test1[1] = 20
grupo1.append(test1[:])
print(f'15:', grupo1)

# Inserindo dados em listas com a estrutura 'for'
grupo2 = []
info = []
for i in range(0, 5):
    info.append(str(input('Nome: ')))
    info.append(int(input('Idade: ')))
    grupo2.append(info[:])
    info.clear()
print(f'16:', grupo2)

# Analisando dados em listas com a estrutura 'for'
qtmai = qtmen = 0
for i in grupo2:
    if i[1] >= 21:
        print(f'17| {i[0]} é maior de idade.')
        qtmai += 1
    else:
        print(f'17| {i[0]} é menor de idade.')
        qtmen += 1
print(f'18: Qtd maiores: {qtmai}')
print(f'19: Qtd menores: {qtmen}')
