# Jogo de Adivinhação
from random import randint
from os import system as sys
sys('cls')

secreto = randint(1, 100)

while True:
    try:
        respostaUsuario = int(
            input('Adivinhe qual número o computador pensou entre 1 e 100: '))

        if respostaUsuario == secreto:
            print('\nVocê acertou!')
            break
        else:
            respostaUsuario = int(input('Você errou! Tente novamente: '))

    except Exception as e:
        print(f'Houve um erro inesperado: {e}')
