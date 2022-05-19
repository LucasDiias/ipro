from os import system as sys
sys('cls')

def media(media1, media2, media3, media4): 
  mediaF = (media1 + media2 + media3 + media4)/4
  print(f'Media final: {mediaF}')

def main():
  media1 = float(input('Informe a primeira media: ').replace(',','.'))
  media2 = float(input('Informe a segunda media: ').replace(',','.'))
  media3 = float(input('Informe a terceira media: ').replace(',','.'))
  media4 = float(input('Informe a quarta media: ').replace(',','.'))

  media(media1, media2, media3, media4)

if __name__ == '__main__':
  main()