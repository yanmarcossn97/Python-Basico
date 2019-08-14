n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
'''if n1 > n2:
    if n1 > n3:
        print('Maior numero: {}'.format(n1))
        if n2 > n3:
            print('Menor número: {}'.format(n3))
        else:
            print('Menor número: {}'.format(n2))
    else:
        print('Maior número: {}'.format(n3))
        print('Menor número: {}'.format(n2))
else:
    if n2 > n3:
        print('Maior número: {}'.format(n2))
        if n1 > n3:
            print('Menor número: {}'.format(n3))
        else:
            print('Menor número: {}'.format(n1))
    else:
        print('Maior número: {}'.format(n3))
        print('Menor número: {}'.format(n1))'''
Maior = n1
if n2 > n1 and n2 > n3:
    Maior = n2
if n3 > n1 and n3 > n2:
    Maior = n3
Menor = n1
if n2 < n1 and n2 < n3:
    Menor = n2
if n3 < n1 and n3 < n2:
    Menor = n3
print('Maior número: {}'.format(Maior))
print('Menor número: {}'.format(Menor))
