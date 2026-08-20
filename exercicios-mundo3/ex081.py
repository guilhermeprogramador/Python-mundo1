#Resolução exercicio 081 - Curso em Video
num = []
while True:
    n = int(input('Digite um numero: ')) 
    num.append(n)
    
    parada = input('Quer continuar? [S/N] ').upper()
    if parada == 'N':
        break

print(f'Foram digitados {len(num)} numeros')
print(f'Os numeros digitados são {sorted(num)}')

if num.count(5) == True:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
