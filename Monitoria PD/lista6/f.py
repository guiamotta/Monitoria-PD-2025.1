matriz = []
for l in range(10):
  matriz.append(input().split())
for l in range(10):
  for c in range(10):
    if matriz[l][c] == "t":
      if (l>0 and matriz[l-1][c]=="*") or \
        (l<9 and matriz[l+1][c]=="*") or \
        (c>0 and matriz[l][c-1]=="*") or \
        (c<9 and matriz[l][c+1]=="*"):
        matriz[l][c] = "p"
for l in range(10):
  print(*matriz[l])