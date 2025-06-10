N, M = map(int, input().split())
pedacos = [int(i) for i in input().split()]
congestionamento = [int(i) for i in input().split()]
pedacos2 = [int(i) for i in input().split()]
congestionamento2 = [int(i) for i in input().split()]
total = total2 = 0
for i in range(N):
  total += pedacos[i]*congestionamento[i]
for i in range(M):
  total2 += pedacos2[i]*congestionamento2[i]
if total >= total2:
  print("TRAJETO 2")
else:
  print("TRAJETO 1")
