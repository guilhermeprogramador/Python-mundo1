#Resolução exercicio 072 - Curso em Video
escrito = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um numero: '))

while True:
    if num < 0 or num > 20:
        num = int(input('Digite novamente, você não digitou um numero valido: '))
    else:
        print(f'Você digitou o numero {escrito[num]}')
        break

