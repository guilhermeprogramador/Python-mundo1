#Resolução do exercicio 042 - Curso em Video 

l1 = int(input('Digite o lado 1: '))
l2 = int(input('Digite o lado 2: '))
l3 = int(input('Digite o lado 3: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 and l1 == l3 and l2 == l3:
        print('Equilatero')
    elif l1 == l2 or l1 == l3 or l3 == l2:
        print('Isosceles')
    else:
        print('Escaleno')
else:
    print('Não forma um triangulo')
