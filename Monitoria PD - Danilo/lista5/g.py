chave = input()
tamanho = len(chave)
n = int(input())
planetas = []
for i in range(n):
  planetas.append(input())
index = tamanho%n
print(planetas[index])