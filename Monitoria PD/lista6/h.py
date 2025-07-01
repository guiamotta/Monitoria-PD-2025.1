set = int(input())
matriz = []
for l in range(set):
  matriz.append(list(map(int,input().split())))
obj = int(input())
total = []
for l in range(set):
  soma = 0
  if obj == 1:
    soma += matriz[l][0]
  elif obj == 2:
    soma += matriz[l][1]
  elif obj == 3:
    soma += matriz[l][2]
  elif obj == 4:
    soma += matriz[l][3]
  total.append(soma)
print(*total)
print(sum(total))
      