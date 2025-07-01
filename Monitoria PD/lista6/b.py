m, n = map(int, input().split())
matriz = []
for l in range(m):
  matriz.append(list(map(int, input().split())))
char, num = input().split()
num = int(num)-1
soma = 0
if char.lower() == "c":
  for l in range(m):
    soma += matriz[l][num]
if char.lower() == "l":
  for c in range(n):
    soma += matriz[num][c]
print(soma)