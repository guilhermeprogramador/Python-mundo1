#Resolução exercicio 031 - Curso em Video 

km = int(input('Digite a distancia da viagem: '))

if km <= 200: 
    print(f'Sua viagem vai custar R$ {km * 0.50}')
else:
    print(f'Sua viagem vai ustar R$ {km * 0.45}')
