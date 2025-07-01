alfabeto = "abcdefghijklmnopqrstuvwxyz"
k = int(input())
string = input()
resultado = ""
for letra in string:
  pos = 0
  achou = False
  while not achou and pos<26:
    if letra == alfabeto[pos]:
      indice = (pos+k)%26
      resultado += alfabeto[indice]
    pos += 1
print(resultado)
  