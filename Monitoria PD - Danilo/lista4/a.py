n = int(input())
valores = map(int, input().split())
b = int(input())
valores = [n*b for n in valores]
print(*valores)