#Resolução exercicio 082 - Curso em Video
impar = []
par = []
lista = []

while True:
    n = int(input('Digite um numero: '))
    lista.append(n)
    
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    
    p = input('Quer continuar? [S/N] ').upper()
    if p != 'S':
        break

print(f'Os numeros digitados foram {lista}')
print(f'Os numeros para digitados foram {par}')
print(f'Os numeros impares digitados foram {impar}')
