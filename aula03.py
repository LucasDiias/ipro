from random import randint
inicio = 1
fim = 10
tentativas = 0

numero = randint(1, 10)
escolha = int(
    input('Adivinhe um número entre 1 e 10: '))
print(numero)
while escolha != numero and inicio != fim:
    if escolha < numero and escolha >= inicio:
        inicio = escolha + 1
    elif escolha > numero and escolha <= fim:
        fim = escolha - 1

    if inicio == fim:
        print(f'\nPerdeste trouxa, o número era {numero}!')
    else:
        print('Você errou! Tente novamente.')
        escolha = int(input(f'Adivinhe um número entre {inicio} e {fim}: '))
    tentativas += 1

if escolha == numero:
    print(f'\nVocê acertou! O número escolhido pelo computador era: {numero}')

print(f'Você tentou {tentativas} vezes.')
