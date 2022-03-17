soma = 0

print('Insira 5 números a serem somados.\n')

while soma <= 50:
    numero = int(input(f'Insira um inteiro: '))
    soma += numero

# Com While
# i = 0
# while i < 5:
#     numeros += int(input(f'Insira o {i + 1}º inteiro: '))
#     i += 1

# Com For
# for i in range(5):
#     numeros += int(input(f'Insira o {i + 1}º inteiro: '))

print(f'\nA soma dos números inseridos é: {soma}')
