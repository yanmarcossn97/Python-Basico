from time import sleep
import os

print('*    '*11)
print('{:^50}'.format(' CONTAGEM REGRESSIVA PARA O ANO NOVO '))
sleep(1)
for n in range(10, -1, -1):
    print('{:^50}'.format(n))
    sleep(1)
print('{:^50}'.format('BUMM! BUMM! POWW!!'))
print('{:^50}'.format('Feliz ano novo!'))
