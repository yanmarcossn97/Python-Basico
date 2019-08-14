contd = maior = qtmasc = qtfem = 0
while True:
    contd += 1
    print(f'Pessoa {contd}')
    nome = str(input('Nome: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M]/[F]: ')).strip().upper()[0]
    if sexo == 'M':
        qtmasc += 1
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        qtfem += 1
    print()
    cond = ' '
    while cond not in 'SN':
        cond = str(input('ADICIONAR MAIS PESSOAS? [S]/[N] ')).strip().upper()[0]
    print()
    if cond == 'N':
        break
print('-'*35)
print('ANÁLISE:')
print(f'Qtd de pessoas cadastradas: {contd}')
print(f'Qtd de homens: {qtmasc}')
print(f'Qtd de pessoas maiores de idade(18): {maior}')
print(f'Mulheres com menos de 20 anos: {qtfem}')
