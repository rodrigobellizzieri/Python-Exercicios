num = input('Digite um número: ')

if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é Par')
    else:
        print(f'O número {num} é impar')
else:
    print(f'O número ->{num}<- não é um número inteiro')
