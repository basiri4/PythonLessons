a = 1
b = 0
c = 0
i = 0
while a > b:
    a = int(input("Введите число А: "))
    b = int(input("Введите число В, которое большее или равно числу А: "))
print("Четные числа на отрезке между числами А и В:", end=" ")
for i in range(a, b+1):
    if i % 2 == 0: print(i, end=" ")
