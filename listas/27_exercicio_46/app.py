numeros = [10, 1, 50, 3, 20]

menor_valor = numeros[0]

for i in numeros:
  if i < menor_valor:
    menor_valor = i

print("O menor valor é o %d" % menor_valor)