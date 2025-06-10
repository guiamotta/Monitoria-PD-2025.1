C = int(input())
while C<-59 or C>-53:
  D = int(input())
  C += D
  if C>320 or C<-64:
    print("Você está fora do mapa!")
  if C <-59:
    print(f"Camada {C}: Vá para cima para achar diamantes!")
  elif C>-53: 
    print(f"Camada {C}: Vá para baixo para achar diamantes!")
print(f"Camada {C}: Você está na faixa dos diamantes!")