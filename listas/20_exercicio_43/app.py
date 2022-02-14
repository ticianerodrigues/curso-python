loja_de_roupas = ["Blusa", "Calça", "Saia", "Vestido"]

i = 0

item_procurado = input("O que deseja procurar primeiro! ")
item_procurado2 = input(" O que deseja procurar depois? ")

while i < len(loja_de_roupas):
  if loja_de_roupas[i] == item_procurado:
   print("O primeiro item foi encontrado antes %s!" % item_procurado)
   break
  
  elif loja_de_roupas[i] == item_procurado2:
    print("O segundo item foi encontrado depois! %s" % item_procurado2)
    break
  
  i = i +1
 
  

 
