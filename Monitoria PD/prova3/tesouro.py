N, M = map(int, input().split())
tesouro = 0
mapa = []
for i in range(N):
    mapa.append(input().split())

for i in range(N):
    for j in range(M):
        if mapa[i][j] == 'X':
          tesouro += 1
          print(f"Tesouro {tesouro}: {i+1} {j+1}")
          
if tesouro == 0:
  print(f"Sem tesouros na região")
