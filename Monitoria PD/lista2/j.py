q1 = int(input())
base = q1//3
resto = q1%3
if resto == 0:
    print("Vermelho", base)
    print("Azul", base)
    print("Amarelo", base)
if resto == 1:
    print("Vermelho", base+1)
    print("Azul", base)
    print("Amarelo", base)
if resto == 2:
    print("Vermelho", base+1)
    print("Azul", base+1)
    print("Amarelo", base)