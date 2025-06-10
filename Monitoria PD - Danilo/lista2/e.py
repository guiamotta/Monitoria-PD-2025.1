c_grande, c, x = map(int, input().split())
total = (c_grande/c)**3
if x<total:
    print("!Eh possivel")
else:
    print("Eh possivel")