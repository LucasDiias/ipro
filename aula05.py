from os import system as sys

alunos = 'Niaclara', 'Ramon', 'Detetive Will', 'Pedro Danilo', 'Pedro', 'Lucas', 'Rodrigo', 'Sofia', 'Helena', 'Paulo', 'Bia', 'Renata', 'Otávio', 'Maju', 'Carlos Eduardo', 'Vitor Hugo'

presentes = 0

for aluno in sorted(alunos):
    presenca = input(f'{aluno} está presente? (P/A)').upper()

    if presenca == 'P':
        presentes += 1

sys('cls')

print('---'*20)
print('Relatório de Frequência - 921A.2\n')
print(f'Total: {len(alunos)}')
print(f'Presentes: {presentes}')
print(f'Ausentes: {len(alunos) - presentes}')
print('---'*20)
