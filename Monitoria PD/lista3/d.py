n = int(input())
premio = 0
for i in range(n):
    p = int(input())
    if p%3 == 0:
        p += 50
    else:
        p /= 2
    premio += p
print(int(premio))