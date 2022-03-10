pessoas = int(input('Quantas pessoas são ao todo? '))

print()

alunos = 0
alunosNaoVac = 0
alunosUmaOuMais = 0
alunosDuasOuMais = 0

servidores = 0
servidoresNaoVac = 0
servidoresUmaOuMais = 0
servidoresDuasOuMais = 0

outros = 0
outrosNaoVac = 0
outrosUmaOuMais = 0
outrosDuasOuMais = 0

totalNaoVac = 0
totalUmaOuMais = 0
totalDuasOuMais = 0

for i in range(pessoas):
    print('---------------------------------------------------')
    print('''(0) Servidor
(1) Aluno
(2) Outros
''')
    tipo = int(input('Insira sua área de atuação: '))
    doses = int(input(f'Quantas doses a {i+1}ª pessoa tomou? '))

    if tipo == 0:
        servidores += 1
        if doses == 0:
            totalNaoVac += 1
            servidoresNaoVac += 1
        else:
            totalUmaOuMais += 1
            servidoresUmaOuMais += 1
            if doses >= 2:
                totalDuasOuMais += 1
                servidoresDuasOuMais += 1

    if tipo == 1:
        alunos += 1
        if doses == 0:
            totalNaoVac += 1
            alunosNaoVac += 1
        else:
            totalUmaOuMais += 1
            alunosUmaOuMais += 1
            if doses >= 2:
                totalDuasOuMais += 1
                alunosDuasOuMais += 1

    if tipo == 2:
        outros += 1
        if doses == 0:
            totalNaoVac += 1
            outrosNaoVac += 1
        else:
            totalUmaOuMais += 1
            outrosUmaOuMais += 1
            if doses >= 2:
                totalDuasOuMais += 1
                outrosDuasOuMais += 1

print('----------------------------------------------------------------')
print(
    f'Percentual de servidores burros condenados: {servidoresNaoVac / servidores * 100:.2f}%')
print(
    f'Percentual de servidores vacinados com pelo menos uma dose: {servidoresUmaOuMais / servidores * 100:.2f}%')
print(
    f'Percentual de servidores vacinados com mais de uma dose: {servidoresDuasOuMais / servidores * 100:.2f}%')
print('----------------------------------------------------------------')
print(
    f'Percentual de alunos burros condenados: {alunosNaoVac / alunos * 100:.2f}%')
print(
    f'Percentual de alunos vacinados com pelo menos uma dose: {alunosUmaOuMais / alunos * 100:.2f}%')
print(
    f'Percentual de alunos vacinados com mais de uma dose: {alunosDuasOuMais / alunos * 100:.2f}%')
print('----------------------------------------------------------------')
print(
    f'Percentual de outros burros condenados: {outrosNaoVac / outros * 100:.2f}%')
print(
    f'Percentual de outros vacinados com pelo menos uma dose: {outrosUmaOuMais / outros * 100:.2f}%')
print(
    f'Percentual de outros vacinados com mais de uma dose: {outrosDuasOuMais / outros * 100:.2f}%')
print('----------------------------------------------------------------')
print('Dentre os não vacinados:')
print(f'{alunosNaoVac / totalNaoVac * 100} são alunos.')
print(f'{servidoresNaoVac / totalNaoVac * 100} são servidores.')
print(f'{outrosNaoVac / totalNaoVac * 100} são de outra área de atuação.')
print()
print('Dentre os usuários ao menos uma dose:')
print(f'{alunosUmaOuMais / totalUmaOuMais * 100} são alunos.')
print(f'{servidoresUmaOuMais / totalUmaOuMais * 100} são servidores.')
print(f'{outrosUmaOuMais / totalUmaOuMais * 100} são de outra área de atuação.')
print()
print('Dentre os vacinados com mais de uma dose:')
print(f'{alunosDuasOuMais / totalDuasOuMais * 100} são alunos.')
print(f'{servidoresDuasOuMais / totalDuasOuMais * 100} são servidores.')
print(f'{outrosDuasOuMais / totalDuasOuMais * 100} são de outra área de atuação.')
print('----------------------------------------------------------------')