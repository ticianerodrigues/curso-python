produto_a = ["Blusa", "Rosa", 50]
produto_b = ["Vestido", "Preto", 120]
produto_c = ["Saia", "Amarela", 35]

print(produto_a, produto_b, produto_c)

produtos = [produto_a, produto_b, produto_c]

print(produtos[0][1])

print(produtos[2][2])

print(produtos[2][0])

for produtos in produtos:
  print("O produto é: %s e tem a cor %s e o seu preço é: R$%.2f" % (produtos[0], produtos[1], produtos[2]))