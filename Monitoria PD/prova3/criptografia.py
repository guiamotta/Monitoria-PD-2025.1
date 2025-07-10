palavras = input().split()
letras = input().split()
resultado = []
for i in range(len(palavras)):
  numero = 0
  for char in palavras[i].lower():
    if char == letras[i].lower():
      numero += 1
  resultado.append(numero)
print(*resultado, sep="")