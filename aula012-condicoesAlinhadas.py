nome = str(input('Digite o seu nome: '))
if nome == 'Yan Marcos':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'João':
    print('Você tem um nome bíblico.')
elif nome in 'Ana, Diana, Eva, Mônica':
    print('Belo nome femenino.')
else:
    print('Nome normal.')
print('Tenha um bom dia.')
