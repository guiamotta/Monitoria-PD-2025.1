P, N, M = map(int, input().split())
C = 0
base = P/N
for i in range(N):
  parcela = base*((1+(M/100))**i)
  C += parcela
  print(f"Parcela {i+1}: R${parcela:.2f}")
print(f"Total: R${C:.2f}")
print(f"Juros: R${C-P:.2f}")