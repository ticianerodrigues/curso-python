idade = int(input("Qual é sua idade? "))

if idade >= 18:
  print("Pode entrar na balada")
  metodo_de_pagamento = input("Como você vai pagar a entrada? ")
  if metodo_de_pagamento == "dinheiro":
    print("A fila do dinheiro é o numero 1")
  else:
    print("A fila do cartão é o numero 2")
  
else:
 print("Você não pode entrar na balada")
