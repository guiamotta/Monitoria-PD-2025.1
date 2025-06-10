totaldias = int(input())
anos = totaldias//365
meses = (totaldias%365)//30
dias = (totaldias%365)%30
print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")