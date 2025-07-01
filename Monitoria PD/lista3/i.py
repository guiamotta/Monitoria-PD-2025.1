n = int(input())
maior_media = 0
maior_nome = ""
for i in range(n):
    nome = input()
    n1, n2 = map(float, input().split())
    media = (0.3*n1) + (n2*0.7)
    if media>maior_media:
        maior_media = media
        maior_nome = nome
print(maior_nome)
    
