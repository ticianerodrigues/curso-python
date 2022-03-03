def soma_todos(*num):
  soma = 0
  for num in num:
    soma += num
  return soma

s = soma_todos(5,3,8,9,78,46,93)

print(s)

s2 = soma_todos(2,8,9)

print(s2)