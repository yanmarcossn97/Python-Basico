r1 = int(input('Comprimento reta r1(cm): '))
r2 = int(input('Comprimento reta r2(cm): '))
r3 = int(input('Comprimento reta r3(cm): '))
if r1 == r2 and r1 == r3:
    print('Esses valores foram um triângulo.')
    print('Tipo: Equilátero(todos os lados são iguais.).')
elif abs(r2 - r3) < r1 < r2 + r3 and abs(r1 - r3) < r2 < r1 + r3 and abs(r1 - r2) < r3 < r1 + r2:
    if r1 == r2 or r1 == r3 or r2 == r3:
        print('Esses valores formam um triângulo.')
        print('Tipo: Isósceles(dois lados iguais).')
    else:
        print('Esses valores formam um triângulo.')
        print('Tipo: Escaleno(todos os lados são diferentes.).')
else:
    print('Esses valores não formam um triângulo.')
