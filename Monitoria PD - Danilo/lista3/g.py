n = int(input())
moedas = 0
for i in range(n):
    b, p, o = map(int, input().split())
    moedas += b
    moedas += p*5
    moedas += o*25
t = int(input())
final = moedas-t
print(final)