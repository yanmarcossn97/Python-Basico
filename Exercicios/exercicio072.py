numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
escolha = int(input('Escolha um número de 0 a 20: '))
while escolha < 0 or escolha > 20:
    escolha = int(input('ERRO! Tente novamente[0 a 20]: '))
print(f'Você escolheu o número {numeros[escolha]}')
