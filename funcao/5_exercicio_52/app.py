def chama_tamanho_texto(texto):

  resposta = ""

  if len(texto) >= 20:
    resposta = "Texto longo"
  else:
   resposta = "Texto curto"

  return resposta

texto_um = "Você é muito especial para minha vida!"

resp_texto_um = chama_tamanho_texto(texto_um)

print(resp_texto_um)
print(texto_um)

print(chama_tamanho_texto("Olá Mundo!"))

resp_texto_dois = (chama_tamanho_texto("O rato roeu a roupa do rei de Roma"))

print(resp_texto_dois)


