#Resolução exercicio 078 - Curso em Video
num = []

for i in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {i}: ')))

    if i == 0:
        menor = maior = num[i]
    else:
        if menor > num[i]:
            menor = num[i]
        if maior < num[i]:
            maior = num[i]


print(f'Você digitou os valores {num}')

print(f'o maior valor digitado foi {maior} nas posições ', end=' ')
for p, j in enumerate(num):
    if j == maior:
        print(f'{p}...', end='')

print(f'\no menor valor digitado foi {menor} nas posições ', end=' ')
for p, j in enumerate(num):
    if j == menor:
        print(f'{p}...', end='')

