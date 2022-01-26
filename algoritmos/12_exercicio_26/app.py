categoria = int(input("Digite um número do produto: "))

if categoria > 0 and categoria <= 1:
  print("È uma bolsa")
elif categoria > 1 and categoria <= 2:
  print("È um Têns")
elif categoria > 2 and categoria <= 3:
  print("È uma mochila")
else:
  print("Não foi encontrada")

  
