inventario = []
item = input()
while item != "fim":
  inventario.append(item)
  item = input()
nome = input()
if nome in inventario:
  print("item encontrado")
else:
  print("voce ainda nao descobriu este item")