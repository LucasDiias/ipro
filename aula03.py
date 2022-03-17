from random import randint

numero = randint(1, 10)
escolha = int(
    input('Adivinhe o número que o computador escolheu entre 1 e 10: '))

while escolha != numero:
    escolha = int(input('Errou! Tente novamente: '))

print(f'\nVocê acertou! O número escolhido pelo computador era: {numero}')
