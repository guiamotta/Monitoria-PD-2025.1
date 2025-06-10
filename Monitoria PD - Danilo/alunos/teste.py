n = int(input())  # Número total de casas
pulos = []        # Lista com os valores de pulo
pos = 0           # Começa na casa 0 (primeira)
c_visitadas = set()  # Conjunto para armazenar as casas já visitadas

# Lê os valores dos pulos
for _ in range(n):
    x = int(input())
    pulos.append(x)

# Simula os pulos
while 0 <= pos < n:
    if pos in c_visitadas:
        # Já passou por essa casa, entrou em ciclo
        break

    c_visitadas.add(pos)  # Marca a casa como visitada

    # Antes de pular, verifica se já está na última casa
    if pos == n - 1:
        print("true")
        break

    pos += pulos[pos]  # Realiza o pulo

else:
    # Saiu do laço sem chegar na última casa
    print("false")