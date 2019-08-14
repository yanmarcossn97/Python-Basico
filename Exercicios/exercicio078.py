'''maior = 0
valores = []
for c in range(0, 5):
    num = int(input('Insira um valor: '))
    valores.append(num)
    if c == 0 or num < menor:
        menor = num
    if num > maior:
        maior = num
print(f'Valores informados: {valores}')
print(f'Maior valor: {maior}; Posições: ', end='')
for i in range(0, 5):
    if valores[i] == maior:
        print(i, end=', ')
print(f'\nMenor valor: {menor}; Posição: ', end='')
for i in range(0, 5):
    if valores[i] == menor:
        print(i, end=', ')'''
maior = 0
valores = []
for c in range(0, 9):
    valores.append(int(input(f'Valor {c}: ')))
    if c == 0 or valores[c] < menor:
        menor = valores[c]
    elif valores[c] > maior:
        maior = valores[c]
print(f'Valores informados: {valores}')
print(f'Maior valor: {maior}; Posições: ', end='')
for i, iten in enumerate(valores):
    if iten == maior:
        print(f'{i}', end=', ')
print(f'\nMenor valor: {menor}; Posições: ', end='')
for i, iten in enumerate(valores):
    if iten == menor:
        print(f'{i}', end=', ')
