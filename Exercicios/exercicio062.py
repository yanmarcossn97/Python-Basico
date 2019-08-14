n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
x = c = 0
# Em vez de atribuir diretamente a quantidades de termos a 'x'...
# eu atribuo a 'y' que não pode começar com '0'...
# Pela propria logica 'x' ira erdar o valor de 'y'
y = int(input('Quantidade de termos: '))
while y != 0:
    x += y
    while c < x:
        print(n1, end='')
        print(', ' if c < x - 1 else '...', end='')
        n1 += r
        c += 1
    y = int(input('\nDeseja ver mais quantos termos? '))
print('Qtd de termos mostrados: {}'.format(x))
