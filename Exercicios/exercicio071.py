valor = int(input('Valor do saque: '))
c = valor // 100
valor %= 100
l = valor // 50
valor %= 50
xx = valor // 20
valor %= 20
x = valor // 10
valor %= 10
v = valor // 5
valor %= 5
ii = valor // 2
valor %= 2
i = valor
if c != 0:
    print(f'{c} Cédula(s) de R$ 100,00')
if l != 0:
    print(f'{l} Cédula(s) de R$ 50,00')
if xx != 0:
    print(f'{xx} Cédula(s) de R$ 20,00')
if x != 0:
    print(f'{x} Cédula(s) de R$ 10,00')
if v != 0:
    print(f'{v} cédula(s) de R$ 5,00')
if ii != 0:
    print(f'{ii} cédula(s) de R$ 2,00')
if i != 0:
    print(f'{i} Moeda(s) de R$ 1,00')
