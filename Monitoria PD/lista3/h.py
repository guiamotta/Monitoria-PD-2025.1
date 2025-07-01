n = int(input())
casa = 1
flag = 0
for i in range(n):
    x = int(input()) 
    casa += x
    if casa < 1:
        casa = 1
    if casa>= n:
        flag = 1
if flag == 1:
    print("true")
else:
    print("false")