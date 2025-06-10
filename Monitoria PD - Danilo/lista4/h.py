T = int(input())
N = int(input())
dano_macacos = list(map(int, input().split()))
total = 0
for i in range(N):
  total += dano_macacos[i]*T
if total>=28000:
  print("Macacos venceram!")
else:
  print("O BAD venceu!")