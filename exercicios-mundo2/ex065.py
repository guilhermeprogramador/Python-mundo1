#Resolução exercicio 065 - Curso em video

i = ''
cont = num = maior = menor = media = 0

while i != 'N':
    num = int(input('Digite um numero: '))

    if num > maior:
        maior = num
    
    if cont == 0:
        menor = num
    else:
        if menor > num:
            menor = num


    i = str(input('Quer continuar? [S/N]: ')).upper()
    cont += 1
    media += num

print(f'O menor numero digitado foi {menor}, o maior foi {maior}, e a media dos numeros é {media / cont}')
