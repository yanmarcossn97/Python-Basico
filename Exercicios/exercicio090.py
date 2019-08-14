aluno = {}
aluno['nome'] = str(input('Nome do(a) aluno(a): '))
aluno['media'] = float(input('Media: '))
if aluno['media'] >= 7:
    aluno['sit'] = 'Aprovado'
else:
    aluno['sit'] = 'Reprovado'
print('ANÁLISE:')
print('Nome do(a) aluno(a):', aluno['nome'])
print('Média do(a) aluno(a):', aluno['media'])
print('Situação:', aluno['sit'])
