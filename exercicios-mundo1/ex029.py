#Resolução exercicio 029 - Curso em Video 

velocidade = int(input('Digite a sua velocidade: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'Você foi multado, sua velocidade ultrapassou o limite')
    print(f'sua multa é de R$ {multa}')
else:
    print('Você estava dentro do limite de velocidade')
