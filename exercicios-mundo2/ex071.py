#Resolução do exercicio 071 - Curso em Video



saque = int(input('Qual valor você quer sacar? '))
total = saque
ced = 50 
i = 0

while True:
    if total >= ced:
        total -= ced
        i += 1
    else:
        if i > 0:
            print(f'Total de {i} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        i = 0 
        if total == 0:
            break

    
