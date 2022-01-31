# Crie uma lista com 5 valores zerados;
# Faça um loop para percorrer a lista e preencher os valores zerados;
# Os valores devem ser inseridos pelo usuário;
# Imprima o resultado final com print;


lista = [0, 0, 0, 0, 0]

print(lista)

i = 0

while i < 5:
  valor1 = int(input("Digite o primeiro valor: "))
  lista[i] = valor1
  i = i + 1

print(lista)

