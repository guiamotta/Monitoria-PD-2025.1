t = int(input())
flag = 0
while True:
    p = int(input())
    if p==0:
        break
    if p>t and flag==0:
        flag += 1
        print("ALARME")
if flag==0:
    print("O Havai pode dormir tranquilo")