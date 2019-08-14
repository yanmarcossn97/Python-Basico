print('Verificando se uma frase é um PALÍDROMO')
frase = str(input('Digite uma frase: ')).strip().upper()
separada = frase.split()
junta = ''.join(separada)
invertida = ''
for c in range(len(junta) - 1, -1, -1):
    invertida += junta[c]
if invertida == junta:
    print('Normal {} = {} Invertida'.format(junta, invertida))
    print('Essa frase é um PALÍDROMO.')
else:
    print('Normal {} != {} Invertida'.format(junta, invertida))
    print('Essa frase não é um PALÍDROMO.')
