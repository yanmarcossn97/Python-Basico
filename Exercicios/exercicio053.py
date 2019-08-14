print('Verificanado se uma frase é um palíndromo')
frase = str(input('Digite uma frase: ')).strip().upper()

#1 Separando a frase por palavras
separado = frase.split()
# print(separado)

#2 Juntando as palavras novamente(sem espaços)
junto = ''.join(separado)
# print(junto)

#3 Invertendo a frase
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
# print(inverso)

#4 Verificando se a frase invertida é igual à frase que foi junta(#2)
if inverso == junto:
    print('Normal {} = {} invertida'.format(junto, inverso))
    print('Essa frase é um Palíndromo.')
else:
    print('Normal {} != {} invertida'.format(junto, inverso))
    print('Essa frase não é um Palíndromo.')
