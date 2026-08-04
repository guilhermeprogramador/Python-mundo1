#Resolução do exercicio 059 - Curso em video 
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo numero: '))

i = 0

while i != 5:
    j = int(input('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]Sair do programa: '))
    
    if j == 1:
        print(n1 + n2)
    elif j == 2:
        print(n1 * n2)
    elif j == 3:
        if n1 >= n2:
            print(n1)
        else:
            print(n2)
    elif j == 4:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outr numero: '))
    elif j == 5:
        i = j
    
print('Fim do programa')
