#resolução exercicio 022 - Curso em Video

nome = input('digite seu nome: ')

print(f'{nome.upper()} letras maiusculas e {nome.lower()} letras minuscula')

primeiro = nome.split()
print(f'O primeiro nome tem {len(primeiro[0])} letras')

tamanho = len(primeiro[0]) + len(primeiro[1]) + len(primeiro[2])
print(f'O nome tem {tamanho} letras')


