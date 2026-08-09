#Resolução do exercicio 075 - Curso em Video

numeros = int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimos numero: '))

cont = cont_par = 0

for i in numeros: 
    if i == 9:
        cont += 1

    if i % 2 == 0:
        cont_par += 1

print(f'foi digitado os valores {numeros}\n')

print(f'o valor 9 apareceu {cont} vezes\n')

print(f'Os valores pares digitados, sua quantidade foi de {cont_par} valores pares\n')

if 3 in numeros:
    print(f'O valor 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não apareceu em nenhuma posição')

