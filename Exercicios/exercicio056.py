somaidade = 0
hmv = ''
mid = 0
qtmeninas = 0
for c in range(1, 5):
    print('{}º PESSOA'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    somaidade += idade
    sexo = str(input('Sexo[M]/[F]: '))
    if sexo in 'Mm' and idade > mid:
        hmv = nome
        mid = idade
    print()
    if sexo in 'Ff' and idade < 20:
        qtmeninas += 1
mediaidade = somaidade / 4
print('Média de idade do grupo: {} anos.'.format(mediaidade))
print('Homem mais velho: {}'.format(hmv))
print('Qtd de meninas com menos de 20 anos: {}'.format(qtmeninas))
