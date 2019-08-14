cidade = str(input('Digite o nome da sua cidade: ')).strip()
# list = cidade.upper().split()
# print('O nome da cidade começa com "Santo" ? {}.'.format('SANTO' in list[0]))
print('O nome da cidade começa com "Santo"? {}.'.format(cidade[:5].upper() == 'SANTO'))
