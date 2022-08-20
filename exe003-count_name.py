nome = str(input('Digite seu primeiro nome: '))

count = len(nome)
if count <= 4:
    print('seu nome é curto')
elif count == 5 or count == 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
