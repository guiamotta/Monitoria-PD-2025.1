nome, idade, bussola, mapa, po, espada = input().split()
idade = int(idade)
erros = ""
if idade>=12 and bussola=="1" and mapa =="1" and po =="1" and espada == "1":
    print(f"{nome}, condicoes ok! Boa sorte na busca pelo tesouro!")
else:
    if idade<12:
        erros += "Nao possui idade minima; "
    if bussola=="0":
        erros += "Nao possui bussola; "
    if mapa=="0":
        erros += "Nao possui mapa do tesouro; "
    if po=="0":
        erros += "Nao possui po magico; "
    if espada=="0":
        erros += "Nao possui espada magica; "
    print(erros)
    print(f"{nome} nao cumpre todas as condicoes!")
