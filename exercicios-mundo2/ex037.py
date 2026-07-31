#Resolução do exercicio 037 - Curso em Video 

num = int(input('Digite um numero: '))
conversao = int(input('''ESCOLHA PARA QUAL BASE QUER CONVERTER O NUMERO
                  [1] PARA OCTAL
                  [2] PARA HEXADECIMAL
                  [3] PARA BINARIO
                  '''))

if conversao == 1:
    print(f'o numero {num} em OCTAL é {oct(num)}')
elif conversao == 2:
    print(f'o numero {num} em HEXADECIMAL é {hex(num)}')
elif conversao == 3:
    print(f'o numero {num} em BINARIO é {bin(num)}')
else:
    print('Você não digitou uma opção valida')
