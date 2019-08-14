clubesord = ()
tabela = ('Santos', 'Palmeiras', 'Flamengo', 'Atlético MG', 'São Paulo', 'Corinhthians',
          'Botafogo', 'Internacional', 'Ceará SC', 'Bahia', 'Atlético PR', 'Fortaleza',
          'Goiás', 'Grêmio', 'Vasco', 'Fluminense', 'Cruzeiro', 'Chapecoense', 'CSA', 'Avaí')
print('TABELA LIGA BRASILEIRA DE FUTEBOL')
for pos, clube in enumerate(tabela):
    print(f'{pos + 1:2}º: {clube}')
print('\n4 PRIMEIROS COLOCADOS')
for pos in range(0, 4):
    print(f'{pos + 1}º: {tabela[pos]}')
print('\n4 ÚLTIMOS COLOCADOS')
for pos in range(16, 20):
    print(f'{pos + 1}º: {tabela[pos]}')
print('\nCLUBES EM ORDEM ALFABÉTICA')
clubesord = sorted(tabela)
for clube in clubesord:
    print(clube)
print('\nCHAPECOENSE')
print('Posição:', tabela.index('Chapecoense') + 1)
