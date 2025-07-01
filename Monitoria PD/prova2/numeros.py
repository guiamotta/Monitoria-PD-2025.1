n = int(input())
lista = list(map(int, input().split()))
numeros = []
for i in range(n):
  if (lista[i]**2)%3!=0 and ((lista[i])**2)%5!=0:
    numeros.append(lista[i])
if len(numeros)>0:
  print(f"Bruninha, diga {len(numeros)} número(s):", *numeros)
else:
  print("Não tem nenhum!")