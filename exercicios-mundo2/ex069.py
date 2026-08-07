#Resolução do exercicio 069 - Curso em Video
dezoito = cont = homens = mulheres = 0

while True:

    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F]').upper()

    if sexo != 'M' and sexo != 'F':
        while True:
            sexo = input('Sexo: [M/F]').upper()
            if sexo == 'M' or sexo == 'F':
                break
    
    if idade >= 18:
        cont += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        if idade < 20:
            mulheres += 1

    resposta = input('Você quer continuar? [S/N]').upper()
    if resposta == 'N':
        break
print(f'{cont} pessoas tem mais de 18 anos, foram cadastrados {homens} homens e {mulheres} mulheres abaixo dos 20 anos')
