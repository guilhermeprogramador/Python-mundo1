#Resolução do exercicio 043 - Curso em Video

peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Abaixo do peso, seu imc é {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print(f'Peso ideial, seu imc é {imc:.2f}')
elif imc >= 25 and imc < 30:
    print(f'Sobrepeso, seu imc é {imc:.2f}')
elif imc >= 30 and imc < 40:
    print(f'Obesidade, seu imc é {imc:.2f}')
else:
    print(f'Obesidade Morbida, seu imc é {imc:.2f}')

