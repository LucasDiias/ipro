# Maykon Lucas Ferreira Dias e Sofia Pacheco Rizzotto
from os import system as sys
sys('cls') # Dando clear no console

porHora = float(input('Informe quanto você ganha por hora: R$').replace(',', '.'))
horaMes = int(input('Informe quantas horas você trabalha no mês: '))
salario = porHora * horaMes

print(f'Salário a ganhar no mês: R${str(salario).replace(".", ",")}')