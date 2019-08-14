for a in range(1, 6):
    print(a, 'Olá Mundo!')
print('Fim')
# Perceba que a 'c' vai apenas até 5. No 6 ele para.

for b in range(6, 1, -1):
    print(b, 'Olá Mundo!')
print('Fim')
# Perceba agora que a contagem foi apenas até 2. Quando 'i' atingiu o valor 1 ele parou.
# Ou seja, a estrutura 'for' se repete enquanto o valor da variável não tiver atingido o limite.

for c in range(0, 10, 2):
    print(c, 'Olá Mundo!')
print('Fim')
# É possível fazer contagem pulando valores. Para isso basta informar quantas casas deseja pular.

for d in range(15, 0, -3):
    print(d, 'Olá Mundo!')
print('fim')
# Também é possível pular valores em contagem regressiva.

e = int(input('Até quanto deseja contar? '))
for f in range(0, e):
    print(f, 'Olá Mundo!')
print('Fim')
g = int(input('Contagem regressiva: '))
for h in range(g, 0, -1):
    print(h, 'Olá Mundo!')
print('Fim')
# Repetição com intervalo vindo de valor contido em uma variável externa.

i = int(input('De: '))
j = int(input('Até: '))
k = int(input('Passo: '))
for l in range(i, j, k):
    print(l, 'Olá Mundo!')
print('Fim')
# Todos os parãnmetros podem ser passodos pelo usuário.