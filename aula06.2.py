from os import system as sys
sys('cls')

alunos = []

while True:
    aluno = input(
        'Insira um nome de um aluno ou digite [0] para sair: ').strip().lower().title()

    if aluno == '0':
        break

    grupo = input('Insira o grupo desse aluno: ').strip()

    if grupo == '1':
        alunos.insert(0, aluno)
    else:
        alunos.append(aluno)

print(alunos)
