n = int(input())
mapa = map(int, input().split())
s = int(input())
saltos = 0
venceu = True
for i in range(n):
  if mapa[i]<=s and venceu:
    saltos += 1
  else:
    venceu = False
print(saltos)
if venceu:
  print(1)
else:
  print(0)
  