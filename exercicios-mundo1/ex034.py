#Resolução do exercicio 034 - Curso em Video 

salario = int(input('Digite seu salario: '))

print(f'Seu salario é {(salario + (salario * 10/100))}' if salario > 1250 else f'{salario + (salario * 15/100)}')
