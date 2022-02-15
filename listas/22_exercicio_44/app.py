numeros = [1, 2, 3, 4, 5]

qual_numero_quer_encontrar = int(input("Qual número deseja buscar? "))

encontrado = False

for n in numeros:
  if n == qual_numero_quer_encontrar:
    print("O número %d foi encontrado!" % n)
    encontrado = True

if encontrado == False:
  print("Não encontramos o número %d" % qual_numero_quer_encontrar)


