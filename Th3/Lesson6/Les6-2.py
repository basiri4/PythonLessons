a = int(input("Введите число: "))
delitel = 0
for i in range(1, a + 1):
    if a % i == 0: delitel += 1
print("Количество натуральных делителей:", delitel)