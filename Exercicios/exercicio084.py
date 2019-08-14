grupo = []
dados = []
pessmenpeso = []
pessmaipeso = []
cond = ''
menpeso = maipeso = 0
while cond != 'N':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso(Kg): ')))
    grupo.append(dados[:])
    dados.clear()
    cond = str(input('\nCadastrar outra pessoas[S/N]? ')).strip().upper()[0]
for contd, pessoa in enumerate(grupo):
    if contd == 0:
        pessmenpeso.append(pessoa[0])
        pessmaipeso.append(pessoa[0])
        menpeso = maipeso = pessoa[1]
    elif pessoa[1] < menpeso:
        pessmenpeso.clear()
        pessmenpeso.append(pessoa[0])
        menpeso = pessoa[1]
    elif pessoa[1] == menpeso:
        pessmenpeso.append(pessoa[0])
    elif pessoa[1] > maipeso:
        pessmaipeso.clear()
        pessmaipeso.append(pessoa[0])
        maipeso = pessoa[1]
    elif pessoa[1] == maipeso:
        pessmaipeso.append(pessoa[0])
print(f'Total de pessoas cadastradas: {len(grupo)}')
print(f'Menor peso cadastrado: {menpeso} Kg ', end='')
for p in pessmenpeso:
    print(f'{p}', end=', ')
print(f'\nMaior peso cadastrado: {maipeso} Kg ', end='')
for p in pessmaipeso:
    print(f'{p}', end=', ')
