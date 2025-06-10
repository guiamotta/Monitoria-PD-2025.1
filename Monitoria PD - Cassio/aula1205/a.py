total = 0
num = 0
while True:
  nota = float(input())
  if nota<0:
    break
  total += nota
  num += 1
print(f"Media: {total/num:.2f}")