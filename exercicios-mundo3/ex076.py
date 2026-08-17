#Resolução exercicio 076 - Curso em Video

lista = ('farinha', 2.50, 'Bolacha', 1, 'Pão', 2, 'Livro', 35)

for i in range(0, len(lista)):
    if i % 2 == 0: 
        print(f'\n{lista[i]:.<30}', end=' ')
    else:
        print(f'R${lista[i]:>4.2f}', end=' ')  
