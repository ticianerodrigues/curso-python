lista = ["Maria", "Guilherme", "Ana"]

nova_lista = lista[:]

print(lista)
print(nova_lista)

nova_lista[0] = "Paula"

print(nova_lista)
print(lista)