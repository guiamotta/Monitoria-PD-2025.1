N = int(input())
nomes = []
for i in range(N):
  nomes.append(input().capitalize())
nomes = sorted(nomes)
for nome in nomes:
  print(nome)