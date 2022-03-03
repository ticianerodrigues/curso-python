def multiplicacao(*args):
  resultado = 1
  for numero in args:
    resultado *= numero
  return resultado

valor = multiplicacao(2,3)
print(valor)
