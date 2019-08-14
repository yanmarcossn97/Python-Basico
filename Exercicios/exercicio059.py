n1 = int(input('Digite um número(N1): '))
n2 = int(input('Digite outro número(N2): '))
print()
print('MENU \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair do programa')
print()
x = int(input('Escolha uma opção: '))
maior = n1
while x != 5:
    if x == 1:
        soma = n1 + n2
        print('A soma desses valores é igual a: {}'.format(soma))
        print()
    elif x == 2:
        prod = n1 * n2
        print('O produto dos valores é: {}'.format(prod))
        print()
    elif x == 3:
        if n2 > n1:
            maior = n2
        print('Maior número: {}'.format(maior))
        print()
    elif x == 4:
        n1 = int(input('Novo valor para N1: '))
        n2 = int(input('Novo valor para N2: '))
        print()
    elif x < 1 or x > 5:
        print('ERRO! Opção inválida.')
        print()
    x = int(input('Escolha uma opção: '))
print('ACABOU!')
