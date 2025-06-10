n = int(input())
forcas = map(int, input().split())
f = int(input())
selecionados = []
for i, forca in enumerate(forcas):
  if forca >= f/2:
    selecionados.append(i)
print(*selecionados)