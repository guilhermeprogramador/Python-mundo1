#Resolução exercicio 052 - Curso em Video

num = int(input('Digite um numero: '))

cont = 0

for i in range(1, num + 1):
    if num % i == 0:
        cont += 1

if cont > 2:
    print('O numero não e primo')
else:
    print('O numero e primo')
