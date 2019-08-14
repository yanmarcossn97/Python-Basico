import random

# random.choice(list) - escolhe aleatoriamente um item de uma lista
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('quarto aluno: '))
list = [a1, a2, a3, a4]
ch = random.choice(list)
print('Aluno(a) sorteado(a): {}.'.format(ch))
