n = int(input("Введите количество чисел: "))
a = list(map(int, input(f"Введите {n} чисел через пробел: ").split()))
b = set(a[:n])
print("Количество разных чисел:",len(b))