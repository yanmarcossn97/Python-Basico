r1 = int(input('Comprimento da reta r1(cm): '))
r2 = int(input('Comprimento da reta r2(cm): '))
r3 = int(input('Comprimento da reta r3(cm): '))
if abs(r2-r3) < r1 < r2 + r3 and abs(r1-r3) < r2 < r1 + r3 and abs(r1-r2) < r3 < r1 + r2:
    print('Esses valores formam um  triângulo.')
else:
    print('Esses valores não formam um triângulo.')
