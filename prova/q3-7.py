# Maykon Lucas Ferreira Dias e Sofia Pacheco Rizzotto
from os import system as sys
sys('cls') # Dando clear no console

secreta = list('FEDERAL')
tracos = list("_" * len(secreta))
chutes = []

print('Jogo da Forca')
print(f'Palavra secreta: {"".join(tracos)}')

while tracos != secreta:
  chute = input('\nDigite seu chute: ').strip().upper()

  if len(chute) > 1:
    print('Você precisa chutar uma letra por vez.')
  elif not chute.isalpha():
    print('Você só pode digitar letras')
  else:
    if chute not in chutes:
      if chute in secreta:
        chutes.append(chute)
        i = 0
        while i < len(secreta):
          letra = secreta[i]
          if chute == letra:
            tracos[i] = chute
          i += 1
        print('Você acertou uma letra!')
        print("".join(tracos))
      else:
        chutes.append(chute)
        print('Não existe essa letra na palavra secreta.')
    else:
      print('Você já deu esse chute antes.')

print(f'Parabéns! Você acertou em {len(chutes)} chutes.')