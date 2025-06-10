n, t = map(int, input().split())
peixes = 0
for i in range(n):
    h = int(input())
    t -= h
    if t >= 0:
        peixes += 1
print(peixes)
        
        