livros = {
  "O Pequeno Príncipe": 350,
  "Dom Casmurro": 500,
  "O Conde de Monte Cristo": 120,
  "Eu, Robô": 50
}

print(livros)

for livro in livros:
  print("O livro %s tem %d páginas" % (livro, livros[livro]))
