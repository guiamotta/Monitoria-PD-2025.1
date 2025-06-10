tipo = input()
dS, dM, dH = map(float, input().split())
if tipo == "S":
    voltas = int(80/dS)
    print(voltas)
if tipo == "M":
    voltas = int(80/dM)
    print(voltas)
if tipo == "H":
    voltas = int(80/dH)
    print(voltas)




