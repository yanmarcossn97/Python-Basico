nome = input('Digite seu nome: ')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
d = n1 - n2
p = n1 * n2
q = n1 / n2
di = n1 // n2
rd = n1 % n2
pot = n1**n2
rz = n1**(1/n2)
print('-'*52)
print('Prazer em conhece-lo {}.'.format(nome))
print('Prazer em conhece-lo {:30}.'.format(nome))
print('Prazer em conhece-lo {:>30}.'.format(nome))
print('Prazer em conhece-lo {:<30}.'.format(nome))
print('Prazer em conhece-lo {:^30}.'.format(nome))
print('Prazer em conhece-lo {:-^30}.'.format(nome))
print('-'*52)
print('Soma {}; Difereça {};'.format(s, d, p, q), end=' ')
print('Produto {}; Quociente {:.3f}.'.format(p, q))
print('Divisão inteira {}; Resto da divisão {}; \nPotência {}; Raiz {}.'.format(di, rd, pot, rz))
