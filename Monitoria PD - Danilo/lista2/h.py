a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())
a = a1 + a2 + a3
b = b1 + b2 + b3
if a >= 10 or b >= 10:
    if a==b:
        print("A partida ainda nao acabou!")
    elif a>b:
        print("O time A deve recuar agora!")
    else: 
        print("O time B deve recuar agora!")
else:
    print("A partida ainda nao acabou!")