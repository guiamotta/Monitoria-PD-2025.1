n = int(input())
identificadores = list(map(int, input().split()))
poderes = list(map(int, input().split()))
lista_media = poderes.copy()
lista_media.remove(max(lista_media))
lista_media.remove(min(lista_media))
media_poderes = sum(lista_media)/len(lista_media)
final = []
for i in range(n):
  if poderes[i] > media_poderes:
    final.append(identificadores[i])
print(*final)