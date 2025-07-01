d = int(input())
matriz = []
soma = 0
for l in range(d):
    matriz.append(list(map(int, input().split())))
for l in range(d):
  for c in range(d):
    if l==c:
      soma+= matriz[l][c]
print(soma)