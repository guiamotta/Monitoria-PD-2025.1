matriz = []
acesso = True
for i in range(9):
    matriz.append(list(map(int, input().split())))

for i in range(9):
    if matriz[i][i] % 2 == 0:
      acesso = False

if matriz[4][4] != 1:
  acesso = False

if acesso: 
  print("Acesso permitido")
else:
  print("Acesso negado")
