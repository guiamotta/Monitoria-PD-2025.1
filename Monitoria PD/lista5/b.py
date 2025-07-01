consoantes = "bcdfghjklmnpqrstvwxyz"
N, T = map(int, input().split())
for i in range(N):
  num = 0
  titulo = input()
  for letra in titulo:
    if letra in consoantes:
      num += 1
  if num > T:
    print(0)
  else:
    print(1)