#Resolução exercicio 066 - Curso em Video

n = s = cont = 0

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    cont += 1

print(f'Foram digitados {cont} numeros, a soma deles é {s}')
