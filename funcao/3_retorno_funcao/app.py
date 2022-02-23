from pyrsistent import b


def saudacao(nome):
  return "Olá %s" % nome

sds = saudacao("Matheus")

print(sds + ". Tudo bem?")

def soma(a, b):
  return a + b

s = soma(5, 7)
d = soma(5,3)

print(s)

print(s + 6)

print(s + d)

def profissao(nome):

  p = ""

  if nome == "Matheus":
    p = "Programador"
  else:
    p = "Não identificado"
  
  return p

prof = profissao("João")

print(prof)

prof_n = profissao("Matheus")

print(prof_n)