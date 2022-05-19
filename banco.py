from os import system as sys
sys('cls')

saldo = 0

def verSaldo():
  print(f'\nSeu saldo atual é de: {saldo}')
  input()

def depositar(deposito):
  global saldo
  print('\nOperação de Depósito')
  saldo += deposito
  print(f'Você realizou um depósito no valor de R${deposito}')
  verSaldo()
  input()

def sacar(saque):
  global saldo
  if saque > saldo:
    print('\nOperação de Saque')
    saldo -= saque
    print(f'Você realizou um saque no valor de R${saque}')
    verSaldo()
  else:
    print('Saldo insuficiente, operação cancelada.')
  input()

def main():
  print('SIMULAÇÃO DE CONTA BANCÁRIA')
  print('\nOpções:\n[1] Ver Saldo\n[2] Depositar\n[3] Sacar\n[4] Sair\n')

  while True:
    opcao = int(input('Qual operação deseja realizar: ').strip())

    if opcao == 1:
      verSaldo()
    elif opcao == 2:
      valorDeposito = float(input('Quanto deseja depositar: '))
      depositar(valorDeposito)
    elif opcao == 3:
      valorSaque = float(input('Quanto deseja sacar: '))
      sacar(valorSaque)
    elif opcao == 4:
      print('Fim da operação.')
      break

if __name__ == '__main__':
  main()