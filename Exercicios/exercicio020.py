from random import shuffle
# import random
# random.shuffle(list) - embaralha items de uma lita
# shufle(list) - embaralha itens de uma lista
a1 = str(input('Aluno(a) 1: '))
a2 = str(input('Aluno(a) 2: '))
a3 = str(input('Aluno(a) 3: '))
a4 = str(input('Aluno(a) 4: '))
a5 = str(input('Aluno(a) 5: '))
list = [a1, a2, a3, a4, a5]
# random.shuffle(list)
shuffle(list)
print('A ordem de apresentação será: ')
print(list)
