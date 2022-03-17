soma = 0

print('Insira 5 números a serem somados.\n')

while soma <= 50:
    numero = int(input(f'Insira um inteiro: '))
    soma += numero

print(f'\nA soma dos números inseridos é: {soma}')
