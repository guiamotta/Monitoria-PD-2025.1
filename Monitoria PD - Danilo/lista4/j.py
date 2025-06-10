N = int(input())
fases = [int(i) for i in input().split()]
M = int(input())
vida = M
morreu = False
for i in range(N):
  if fases[i]==1:
    vida = M
  if fases[i]>=2:
    vida -= fases[i]
  if vida<=0:
    morreu = True
if morreu:
  print("You Died")
else:
  print("Yes, you can")
