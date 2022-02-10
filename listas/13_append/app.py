from ctypes.wintypes import PLARGE_INTEGER


lista = [0,1,2,3,4]

lista.append(5)

print(lista)

nomes = ["Paulo", "Jõao"]

nomes.append("Pedro")

print(nomes)

if nomes[2] != "Maria":
 nomes.append("Maria")

print(nomes)
