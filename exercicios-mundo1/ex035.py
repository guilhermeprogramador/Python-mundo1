#Resolução do exercicio 035 - Curso em Video 

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Sim, e possivel formar um triangulo')
else:
    print('Não e possivel formar um triangulo')

