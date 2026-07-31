#Resolução do exercicio 037 - Curso em Video 

num = int(input('Digite um numero: '))
conversao = input('Digite qual conversão quer fazer? Octal, Binario ou Hexadecimal')

convert = conversao.upper()
x = []
resto = num % 8

if convert == 'OCTAL':
    while (x != 0):
        x.append(num % 8)
print(x)
