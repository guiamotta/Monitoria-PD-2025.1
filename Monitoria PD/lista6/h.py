fileira, col = map(int, input().split())
matriz = []
soma = 0
especial = True
for l in range(fileira):
  linha = list(map(int, input().split()))
  matriz.append(linha)
  soma_aux = sum(linha)
  if l == 0: 
    soma = soma_aux
  elif soma_aux != soma:
    especial = False
  soma_aux = 0
  for c in range(col):
    soma_aux += matriz[l][c]
  if soma_aux != soma:
    especial = False
if especial:
  print("Sim")
else:
  print("Nao")