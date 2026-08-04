#Resolução exercicio 064 - Curso em Video

i = 0 
cont = 0 
j = 0
p = 1 

while i != p :
    num = int(input('Digite o numero: '))
    if num == 999:
        p = num
        i = p
    else: 
        s = num + j
    j += num

    cont += 1

print(f'Foram digitados {cont - 1} numeros, a soma entre eles é {s}')
