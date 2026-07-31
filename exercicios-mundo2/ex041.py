#Resolução do exercicio 041 - Curso em Video

ano = int(input('Digite o ano que você nasceu: '))

idade = 2026 - ano

if idade <= 9:
    print('mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade == 20:
    print('Senior')
else: 
    print('Master')
