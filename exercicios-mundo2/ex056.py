#Resolução do exercico 056 - Curso em Video

media = 0
velho = 0
mulheres_20 = 0

for i in range(1, 5):
    
    nome = input(f'Digite seu nome, pessoa {i}: \n')
    idade = int(input(f'Digite sua idade pessoa {i}: \n'))
    sexo = int(input(f'Qual o seu sexo pessoa {i}, 1 para mulher e 2 para homem: \n'))
    
    if i == 1:
        velho = idade
    else:
        if idade > velho:
            velho = idade
    
    if sexo == 1 and idade < 20:
        mulheres_20 += 1

    media += idade

print(f'a media de idade é {media / 4}, a pessoa mais velha do grupo tem {velho} e no grupo tem {mulheres_20} mulheres abaixo dos 20')
