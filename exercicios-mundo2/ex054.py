#Resolução exercicio 054 - Curso em Video

maior = 0
menor = 0

for i in range(0, 7):
    ano = int(input('Digite o ano que você nasceu: '))

    if 2026 - ano < 18:
        menor += 1
    else:
        maior += 1

print(f'{maior} são maiores. {menor} são menores')


