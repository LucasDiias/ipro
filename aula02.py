numeros = 0

print('Insira 5 números a serem somados.\n')

for i in range(5):
    numeros += int(input(f'Insira o {i + 1}º inteiro: '))

print(f'\nA soma dos números inseridos é: {numeros}')
