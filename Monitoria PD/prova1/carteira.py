A, B, C = map(int, input().split())

P = int(input())

numero = 0
if ((A*50)+(B*10)+(C*5))<P: 
    print("Pedrinho está liso")
else:
    if A > 0:
        if A*50 >= P:
            numero += P//50
            P -= (P//50)*50
        else:
            numero += A
            P -= A*50
    if B > 0:
        if B*10 >= P:
            numero += P//10
            P -= (P//10)*10
        else:
            numero += B
            P -= B*10
    if C > 0:
        if C*5 >= P:
            numero += P//5
            P -= (P//5)*5
        else:
            numero += C
            P -= C*5    
    if P>0:
        numero += 1
    print(f"Pedrinho usará {numero} cédula(s)")