a, b, c = map(int, input().split())
delta = b**2 - (4*a*c)
if delta>=0:
    x1 = (-b + (delta**(1/2)))/(2*a)
    x2 = (-b - (delta**(1/2)))/(2*a)
    if x1 == x2:
        print(f"{x1:.2f}")
    else:
        print(f"{x1:.2f} {x2:.2f}")
else:
    print("Nao existem")