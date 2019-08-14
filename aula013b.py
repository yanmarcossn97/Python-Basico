s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('A soma dos valores informados é: {}'.format(s))
# A expressão (s += n) equivale a (s = s + n)