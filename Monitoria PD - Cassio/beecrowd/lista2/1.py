x, y = map(int, input().split())
if x == 1: 
    total = 4.00
elif x==2:
    total = 4.50
elif x==3:
    total = 5.00
elif x==4:
    total = 2.00
elif x==5:
    total = 1.50
    
total = total * y
print(f"Total: R$ {total:.2f}")