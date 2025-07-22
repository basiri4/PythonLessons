a = list(map(int, input(f"Введите массив чисел №1 через пробел: ").split()))
b = list(map(int, input(f"Введите массив чисел №2 через пробел: ").split()))

am = set(a)
bm = set(b)

print("Одинаковых чисел в двух массивах: ", len(am.intersection(bm)))