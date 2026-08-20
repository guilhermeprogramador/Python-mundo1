#Resolução exercicio 080 - Curso em Video
numeros = []
for i in range(0,5):
    n = int(input('Digite um numero: '))
    
    if i == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado na ultima posição')
    else:
        j = 0
        while j < len(numeros):
            if n <= numeros[j]:
                numeros.insert(j, n)
                print(f'Adicionando na posição {j}')
                break
            j += 1
    
print(f'Os valores digitados em ordem são {numeros}')
