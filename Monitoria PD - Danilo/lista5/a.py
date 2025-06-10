nome = input()
vagas = int(input())
flag = False
for i in range(vagas):
  aprovado = input()
  if aprovado == nome:
    flag = True
if flag:
  print("PARABENS")
else:
  print("Vamos esperar a 2a chamada")