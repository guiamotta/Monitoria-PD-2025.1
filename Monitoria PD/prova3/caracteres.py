n = int(input())
vogais = "aeiou"
notvogais = "aeiou "
titulos = []
resultados = []
for i in range(n):
  titulos.append(input())
for i in range(n):
  v = c = 0
  for letra in titulos[i].lower():
    if letra in vogais:
      v += 1
    elif letra not in notvogais:
      c += 1 
  print(f"'{titulos[i]}' - V:{v} / C:{c}")
  