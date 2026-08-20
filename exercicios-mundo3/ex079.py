#Resolução exercicio 079 - Curso em Video
num = []

while True:
    i = int(input('Digite um numero: ')) 

    if i not in num:
        num.append(i)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado')

    parada = input('Quer continuar? [S/N]').upper()
    if parada != 'S':
        break

num.sort()
print(f'Os numeros digitados foram {num}')
