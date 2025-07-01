p = int(input())
a_alberto = m_alberto = a_bruno = m_bruno = 0
for i in range(p):
    a, m = map(int, input().split())
    a_alberto += a
    m_alberto += m
for i in range(p):
    a, m = map(int, input().split())
    a_bruno += a
    m_bruno += m
kd_alberto = a_alberto/m_alberto
kd_bruno = a_bruno/m_bruno
if kd_alberto > kd_bruno:
    print("Parabens Alberto!")
    print(f"{kd_alberto:.2f}")
elif kd_alberto < kd_bruno:
    print("Parabens Bruno!")
    print(f"{kd_bruno:.2f}")
else:
    print("Empate")