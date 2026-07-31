#Resolução do exercicio 039 - Curso em Video

ano = int(input('Digite o ano que você nasceu: '))

if (2026 - ano) < 18:
    print(f'Você ainda vai se alistar, falta {18 - (2026 - ano) } anos')
elif (2026 - ano) == 18:
    print('Já está na hora de se alistar')
else:
    print(f'Você já passou {(2026 - ano) - 18} anos do alistamento')

