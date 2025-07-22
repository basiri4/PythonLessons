n = int(input("Введите количество чисел: "))
a = list(map(int, input("Введите массив чисел через пробел: ").split()))
b = []
b.append(a[n-1])
for i in range(n-1): 
    b.append(a[i])
print(b)
