N, M = map(int, input().split())
produtos = input().split()
precos = [float(i) for i in input().split()]
parcelas = [int(i) for i in input().split()]
compras = []
valores = []
prestacoes = []
valor_mensal = 0
for i in range(N):
  parcela = precos[i]/parcelas[i]
  valor_mensal += parcela
  if valor_mensal<=M:
    compras.append(produtos[i])
    valores.append(parcela)
    prestacoes.append(parcelas[i])
  else:
    valor_mensal -= parcela
for i in range(len(compras)):
  print(f"{compras[i]}: R${valores[i]:.2f}/mês em {prestacoes[i]}x")
if len(compras)==0:
  print("Alfredo está sem dinheiro")