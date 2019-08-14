num = contd = soma = maior = menor = 0
cond = 'S'
while cond == 'S':
    num = int(input('Digite um número: '))
    soma += num
    contd += 1
    if contd == 1:
        menor = num
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    cond = str(input('Deseja informar outro número[S]/[N]? ')).upper()
    print()
media = soma / contd
print('ANÁLISE:')
print('Média: {:.1f}'.format(media))
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
