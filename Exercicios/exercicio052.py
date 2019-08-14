print('Verificando se um número é primo')
num = int(input('Informe um número inteiro: '))
qtdiv = 0
ordiv = 1
for c in range(1, num + 1):
    if num % c == 0:
        print('{}º divisor: {}'.format(ordiv, c))
        ordiv += 1
        qtdiv += 1
print('Qtd divisores:', qtdiv)
if qtdiv == 2:
    print('Esse número é primo.')
else:
    print('Esse número não é primo.')
