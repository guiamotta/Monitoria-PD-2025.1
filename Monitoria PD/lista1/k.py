T, D = map(int, input().split())
V, P = map(int, input().split())
valor_pedagios = (T//D)*P
valor_km = T*V
print(valor_pedagios + valor_km)