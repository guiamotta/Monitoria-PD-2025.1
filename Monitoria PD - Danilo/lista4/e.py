n = int(input())
eventos = map(int, input().split())
x = int(input())
total = 0
for i in range(n):
  if eventos[i] == x:
    total += 1
print(total)
