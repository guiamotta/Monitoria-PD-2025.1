n, m = map(int, input().split())
matriz = []
lugares_protegidos = 0
for l in range(n):
  matriz.append(list(map(int, input().split())))
for l in range(n):
  for c in range(m):
    if l>0 and c>0 and l<n-1 and c<m-1:
      vizinhos = []
      vizinhos.append(matriz[l-1][c])
      vizinhos.append(matriz[l+1][c])
      vizinhos.append(matriz[l][c-1])
      vizinhos.append(matriz[l][c+1])
      impares = 0
      for item in vizinhos:
        if item%2==1:
          impares += 1
      if impares == 4:
        lugares_protegidos += 1
if lugares_protegidos >= 1:
  print("Ufa!")
else:
  print("Socorro!")