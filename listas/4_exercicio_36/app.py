# Crie uma lista com 5 notas de provas de um aluno;
# Faça um loop que calcula a média das notas;
# Imprima o resultado final;

notas = [8, 3, 10, 5, 10]

i = 0

soma_das_notas = 0

while i < 5:
  soma_das_notas = soma_das_notas + notas[i]
  i = i + 1

media = soma_das_notas / 5

print("O aluno teve a média %.1f na materia x" % media)







