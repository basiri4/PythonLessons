n = int(input("Введите число: "))
zeros = 0
while n > 0:
    a = int(input("Введите очередное число: "))
    if a == 0: zeros += 1
    n -= 1

print("Количество чисел, равных нулю:", zeros)
