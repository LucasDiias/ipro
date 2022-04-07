from os import system as sys
sys('cls')

nomes = []

while True:
    nome = input(
        'Insira um nome, ou digite [0] para sair: ').strip().lower().title()

    if nome == '0':
        break

    if nome not in nomes:
        if len(nomes) == 0 or nome > nomes[-1]:
            nomes.append(nome)
        else:
            i = 0
            while True:
                if nome > nomes[i]:
                    i += 1
                else:
                    nomes.insert(i, nome)
                    break
    else:
        print(f'O nome {nome} já está na lista.')

    ultimo = nome

print(nomes)
