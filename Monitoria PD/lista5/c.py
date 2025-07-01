N = int(input())
S = input()
meio = (N//2)
if S[0] != S[meio] and S[0] != S[N-1] and S[meio] != S[N-1]:
  print("Sim")
else:
  print("Nao")