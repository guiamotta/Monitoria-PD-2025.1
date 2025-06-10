import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta <= 0:
    print("A função não tem valores reais")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)

    print(f"O valor de x é {x1} ou {x2}")
