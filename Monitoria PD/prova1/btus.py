largura, comprimento = map(float, input().split())

pessoas = int(input())

btus = ((largura * comprimento) * 800) + ((pessoas - 1) * 700)

print(f"O ar-condicionado deve ter, pelo menos, {btus:.0f} BTUs")