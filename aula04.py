usuarios = 0
soma = 0

i = 1
while True:
    idade = int(input(f'Usuário {i}, informe sua idade ou zero para sair: '))

    if idade == 0:
        break

    soma += idade
    usuarios += 1
    i += 1

if usuarios != 0:
    print(f'A média das idades apresentadas é de: {soma / usuarios:.2f}')
else:
    print('Não há alunos')
