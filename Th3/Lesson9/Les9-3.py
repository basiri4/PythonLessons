a = list(map(int, input(f"Введите массив чисел №1 через пробел: ").split()))
bylo = set()

for i in a:
    if i in bylo:
        print(f"Число {i} было")
    else:
        print(f"Число {i} не было")
        bylo.add(i)