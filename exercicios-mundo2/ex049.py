#Resolução exercicio 049 - Curso em Video
num = int(input('Digite o numero da tabuada: '))

j = 0

for i in range(1, 11):
    j = num * i
    print(f'{num} x {i} = {j}')
print('Fim tabuada')
