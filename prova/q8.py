# Maykon Lucas Ferreira Dias e Sofia Pacheco Rizzotto
from os import system as sys
sys('cls') # Dando clear no console

numero = int(input('Informe um número: ').strip())
fatorial = numero

for i in range(1, numero):
  fatorial = fatorial * i

print(f'O fatorial desse número é: {fatorial}')