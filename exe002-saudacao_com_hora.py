#Recebe a hora e converte o tempo em inteiro
hora = input('Digite a hora atual (hh:mm): ')
if hora.isalpha():
    print('Hora inválida')
else:
    tempo = int(hora[0:2])

    if tempo <= 11:
        print('Tenha um bom dia')
    elif tempo >= 12 and tempo <= 17:
        print('Tenha uma boa tarde')
    else:
        print('Tenha uma boa noite')
