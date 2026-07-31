#Resolução exercicio 040 - Curso em Video 

n1 = int(input('Digite sua nota 1: '))
n2 = int(input('Digite sua nota 2: '))

media = (n1 + n2) / 2

if media < 5:
    print('Reprovado')
elif media >= 5 and media < 6.9:
    print('Recuperação')
else: 
    print('Aprovado')


