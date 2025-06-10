n = int(input())
esmeraldas = map(int, input().split())
c = int(input())
achou = False
for i in range(n):
  if c == esmeraldas[i]:
    achou = True
if achou:
  print(c)
else:
  print(-1)
