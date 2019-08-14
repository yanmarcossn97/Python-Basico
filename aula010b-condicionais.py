n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
m = (n1*2+n2*3+n3*2+n4*3)/10
print('Media final: {:.1f}'.format(m))
if m >= 7:
    print('Resultado: Aprovado.')
else:
    print('Resultado: Reprovado.')
# Condicional reduzida a uma linha
print('Aprovado' if m >= 7 else 'Reprovado')
