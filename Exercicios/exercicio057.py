sexo = str(input('Informe o sexo[M]/[F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo inválido! Tente novamente[M]/[F]: ')).strip().upper()[0]
print('Sexo informado: {}'.format(sexo))
