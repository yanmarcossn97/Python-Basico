n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
m = (n1*2 + n2*3 + n3*2 + n4*3) / 10
print('Média final: {:.1f}'.format(m))
if m >= 7:
    print('Resultado: APROVADO.')
elif 5 <= m < 7:
    print('Resultado final: EM RECUPERAÇÃO.')
else:
    print('Resultado: REPROVADO.')
