#Resolução de exercicios 074 - Curso em Video
from random import randint

num1 = randint(0, 10)
num2 = randint(0, 10)
num3 = randint(0, 10)
num4 = randint(0, 10)
num5 = randint(0, 10)

numeros = (num1, num2, num3, num4, num5)

cont = maior = 0

for i in numeros:
    if cont == 0:
        menor = i
    else:
        if menor > i:
            menor = i
    
    if maior < i:
        maior = i

    cont +=1


print(f'da tupla {numeros}, o menor numero é {menor}, e o maior numero é {maior}')
