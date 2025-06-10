n = int(input())
senhas_impar = []
senhas_par = []
for i in range(n):
  s = int(input())
  if s%2==1:
    senhas_impar.append(s)
  else:
    senhas_par.append(s)
senhas_ordenadas = senhas_impar + senhas_par
for i in senhas_ordenadas:
  print(i)