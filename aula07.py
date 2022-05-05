from os import system as sys
sys('cls')

def main():
  saldo = 0.0

  while True:
    print('******************************************')
    print('Simulação de um sistema de Conta Bancária')
    print('******************************************')
    print('\nOpções:')
    print('1- Ver saldo')
    print('2- Depositar')
    print('3- Sacar')

    opcao = int(input('Escolha uma opção: '))
    print(opcao)
    print()

    if opcao == 1:
      print('*****************')
      print('Opção: Ver saldo')
      print('*****************')
      print(f'Saldo: {saldo}')

    elif opcao == 2:
      print('*****************')
      print('Opção: Depositar')
      print('*****************')
      valorDeposito = float(input('Valor do depósito: '))
      saldo += valorDeposito
    
    elif opcao == 3:
      print('*****************')
      print('Opção: Sacar')
      print('*****************')
      valorSaque = float(input('Valor do saque: '))
      saldo -= valorSaque

    continuar = input('\nDeseja continuar [S] ou [N]? ').strip().upper()
    if continuar == 'N':
      break

if __name__ == '__main__':
  main()