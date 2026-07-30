#Resolução do exercicio 033 - Curso em Video 

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite segundo numero: '))
n3 = int(input('Digite terceiro numero: '))

#calcula o maior
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

#calcula o menor
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3


print(f'{maior} {menor}')

