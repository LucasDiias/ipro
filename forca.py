from os import system as sys
sys('cls')

palavra = list('javascript')
chutes = []

qtdeLetras = len(palavra)
qtdeChutes = qtdeLetras + 6
tracos = list('_' * qtdeLetras)

print(f'''JOGO DA FORCA
Chutes: {qtdeChutes}\n''')
print(''.join(tracos))

try:
    while qtdeChutes > 0 and tracos != palavra:
        chute = input('\nAdivinhe uma letra: ').strip().lower()

        if len(chute) = 1:
            print('Você só pode tentar letras.')
        else:
            if chute not in chutes:
                if chute in palavra:
                    chutes.append(chute)
                    qtdeChutes -= 1
                    i = 0
                    while i < len(palavra):
                        letra = palavra[i]
                        if chute == letra:
                            tracos[i] = chute
                        i += 1

                    print(
                        f'\nVocê acertou uma letra! Você ainda tem {qtdeChutes} chances.\n{"".join(tracos)}')
                else:
                    chutes.append(chute)
                    qtdeChutes -= 1

                    print(
                        f'\nOpa, você errou. Tente novamente, você ainda tem {qtdeChutes} chances!\n{"".join(tracos)}')
            else:
                print(f'Você já falou {chute}, tente novamente.')

    if qtdeChutes == 0:
        print('Suas chances acabaram.')
    elif tracos == palavra:
        print('Você venceu!!!')

except Exception as e:
    print(f'Houve um erro inesperado: {e}')
