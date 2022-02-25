def retorna_lista_par(l):
  nova_lista = []

  for numero in l:
   if numero % 2== 0:
    nova_lista.append(numero)

  return nova_lista

lista = [4, 3, 2, 5, 7, 10]

lista_par = retorna_lista_par(lista)

print(lista_par)

lista2 = [1, 3, 23, 43, 54, 65, 5234, 445]

print(retorna_lista_par(lista2))


