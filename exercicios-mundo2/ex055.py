#Resolução do exercicio 055 - Curso em Video

menor = 0
maior = 0

for i in range(1, 6):
    peso = float(input('Digite seu peso: '))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
        
print(f'{maior:.2f} maior, menor {menor:.2f}')

