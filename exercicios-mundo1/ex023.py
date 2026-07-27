#resolução exercicio 023 - Curso em Vídeo 

#resolução forma matemática
numero_mat = int(input('digite um numero entre 1 e 9999: '))

milhar = numero_mat // 1000 
centena = (numero_mat // 100) - ((numero_mat // 1000) * 10)
dezena = (numero_mat // 10) - ((numero_mat // 100) * 10)
unidade = numero_mat - ((numero_mat // 10) * 10)

print(f'milhar: {milhar}')
print(f'centena: {centena}')
print(f'dezena: {dezena}')
print(f'unidade: {unidade}')

#resolução string 
numero_str = input('digite um numero entre 1 e 9999: ')

print(f'milhar: {numero_str[0]}')
print(f'centena: {numero_str[1]}')
print(f'dezena: {numero_str[2]}')
print(f'unidade: {numero_str[3]}')

