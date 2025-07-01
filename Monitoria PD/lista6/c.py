m, n = map(int, input().split())
matriz = []
for l in range(m):
  matriz.append(list(map(int, input().split())))
p = int(input())
pokemon = 0
for l in range(m):
  for c in range(n):
    if matriz[l][c] == p:
      pokemon += 1
print(f"Ash pegou {pokemon} pokemon")