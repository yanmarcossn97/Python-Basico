from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
pessoa['nasc'] = int(input('Ano de nascimento: '))
anoatual = date.today().year
pessoa['idade'] = anoatual - pessoa['nasc']
pessoa['ctps'] = int(input('Carteira de Trabalho[0 se não tiver]: '))
if pessoa['ctps'] != 0:
    pessoa['anocontrat'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Valor do salário(R$): '))
    pessoa['contrib'] = anoatual - pessoa['anocontrat']
    pessoa['apos'] = pessoa['idade'] + pessoa['contrib']
print('\nANÁLISE...')
for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
