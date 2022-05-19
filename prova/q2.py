# Maykon Lucas Ferreira Dias e Sofia Pacheco Rizzotto
from os import system as sys
sys('cls') # Dando clear no console

sequencia = [0, 1]
limite = int(input('Defina um valor limite para a sequencia de Fibonacci: '))

anterior = 0
atual = 1

while True:
  novo = anterior + atual
  if novo > limite:
    break
  else:
    sequencia.append(novo)

    anterior = atual
    atual = novo

print(f'Sequencia de Fibonacci gerada: {sequencia}')