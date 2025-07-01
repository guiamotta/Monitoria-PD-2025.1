fileira, col = map(int, input().split())
matriz = []
for l in range(fileira):
  matriz.append(list(map(int, input().split())))
for l in range(fileira):
  for c in range(col):
    if c<col-1:
      if matriz[l][c]==0 and matriz[l][c+1]==0:
        print(f"Fileira: {l+1}")
        print(f"Assentos: {c+1} e {c+2}")