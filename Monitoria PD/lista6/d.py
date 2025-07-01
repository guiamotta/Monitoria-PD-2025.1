n, m = map(int, input().split())
matriz = []
x = y = 0
virus_aniquilado = False
for l in range(n):
  matriz.append(list(map(int, input().split())))
for l in range(n):
  for c in range(m):
    if matriz[l][c]==0 and l>0 and c>0 and l<n-1 and c<m-1:
      x = l
      y = c
      if matriz[l-1][c]==1 and matriz[l+1][c]==1 and matriz[l][c-1]==1 and matriz[l][c+1]==1:
        virus_aniquilado = True
if virus_aniquilado:
  print(x, y)
else:
  print(0, 0)