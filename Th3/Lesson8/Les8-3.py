m = int(input("Какая грузоподъемность: "))
n = int(input("Количество рыбаков: "))
ves = []
for i in range(n):
    ves.append(int(input(f"Введите массу {i+1} рыбака: ")))
ves.sort()
ryb_l = 0
ryb_t = n - 1
lodok = 0

while ryb_l <= ryb_t:
    if ves[ryb_l] + ves[ryb_t] <= m:
        ryb_l += 1
    ryb_t -= 1
    lodok += 1

print(f"Понадобится {lodok} лодок")