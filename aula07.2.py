# Operações Matemáticas
from os import system as sys
sys('cls')

def soma(a, b):
  print('\nOperação de Adição')
  print(f'Resultado de {a} + {b} é: {a+b}')

def subtrai(a, b):
  print('\nOperação de Subtração')
  print(f'Resultado de {a} - {b} é: {a-b}')

def multiplica(a, b):
  print('\nOperação de Multiplicação')
  print(f'Resultado de {a} * {b} é: {a*b}')

def divide(a, b):
  print('\nOperação de Divisão')
  print(f'Resultado de {a} / {b} é: {a/b}')

def main():
  print('Operações:\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n')
  operacao = int(input('Informe o número da operação que deseja realizar: ').strip())
  a = float(input('Defina o primeiro valor da operação: ').strip())
  b = float(input('Defina o segundo valor da operação: ').strip())
  
  if operacao == 1:
    soma(a, b)
  elif operacao == 2:
    subtrai(a, b)
  elif operacao == 3:
    multiplica(a, b)
  elif operacao == 4:
    divide(a, b)

if __name__ == '__main__':
  main()