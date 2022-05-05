from os import system as sys
sys('cls')

verde = '\033[1;32m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
azul = '\033[1;34m'
reset = '\033[0;0m'

palavra = list('ergastoplasma')
chances = []
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

qtdeLetras = len(palavra)
qtdeChances = qtdeLetras + 6
tracos = list('_' * qtdeLetras)

print(f'''{azul}JOGO DA FORCA{reset}
Chances: {amarelo}{qtdeChances}{reset}\n''')
print(''.join(tracos) + '\n')

while qtdeChances > 0 and tracos != palavra:
    chute = input(f'{reset}Adivinhe uma letra ou tente a palavra: ').strip().lower()

    if chute == ''.join(palavra):
        tracos = palavra
        break

    if len(chute) > 1 or chute in numeros:
        print(f'{amarelo}Você só pode tentar uma letra.\n')
    elif chute == '' or chute == ' ':
        print(f'{amarelo}Você não digitou nada!\n')
    else:
        if chute not in chances:
            if chute in palavra:
                chances.append(chute)
                
                i = 0
                while i < len(palavra):
                    letra = palavra[i]
                    if chute == letra:
                        tracos[i] = chute
                        qtdeChances -= 1
                    i += 1

                print(
                    f'{verde}Você acertou uma letra! Você ainda tem {amarelo + str(qtdeChances) + verde} chances.\n{reset}{"".join(tracos)}\n')
            else:
                chances.append(chute)
                qtdeChances -= 1

                print(
                    f'{vermelho}Opa, você errou. Tente novamente, você ainda tem {amarelo + str(qtdeChances) + vermelho} chances!\n{reset}{"".join(tracos)}\n')
        else:
            print(f'{amarelo}Você já falou {reset}{chute}{amarelo}, tente novamente.\n')

if qtdeChances == 0:
    print(f'\n{vermelho}Fim da linha! Suas chances acabaram. A palavra era {amarelo}{"".join(palavra)}{vermelho}.{reset}')
elif tracos == palavra:
    print(f'\n{verde}Parabéns, você venceu!!! A palavra era {amarelo}{"".join(palavra)}{verde}.{reset}')
