import loteria

    
print("Game da Mega-Sena (digite sair para finalizar)")
numeros = 0

while True:
   numeros = input("Digite os 6 numeros:")
   if numeros.lower() == 'sair':
       break
   try: 
      result =loteria.sorteio(numeros)
      if result[0] == 'ganhou':
         print(f"Resultado: Você {result[0]} o valor de {result[1]}")
      else:   
         print(f"Resultado: Você {result[0]}") 
   except ValueError as error:
      print("Aconteceu um erro:", error)

print("Fim do game.")