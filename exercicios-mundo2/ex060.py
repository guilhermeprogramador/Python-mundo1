#Resolução do exercicio 060 - Curso em Video

num = int(input('Digite um numero: '))

i = num - 1

while not i == 0:
    
    if i == num - 1:
        fatorial = num * i
    else:
        fatorial = fatorial * i
    i -= 1

print(f'O fatorial de {num} é {fatorial}')

