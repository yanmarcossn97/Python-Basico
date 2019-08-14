frase = str(input('Digite uma frase: ')).strip()
print('Qtd de letras "A" na frase: {}'.format(frase.upper().count('A')))
print('Posição da primeira letra "A": {}'.format(frase.upper().find('A')+1))
print('Posição da última letra "A": {}'.format(frase.upper().rfind('A')+1))
