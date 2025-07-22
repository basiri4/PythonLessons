a = int(input())
if (a > 0) and (a % 2 == 0):
    print("Положительное четное число")
elif (a > 0) and (a % 2 != 0):
    print("Положительное нечетное число")
elif (a < 0) and (a % 2 == 0):
    print("Отрицательное четное число")
elif (a < 0) and (a % 2 != 0):
    print("Отрицательное нечетное число")
elif (a == 0):
    print("Нулевое число")
else:
    print("не число")
s = int(input("Инвестиции: "))
m = int(input("Инвестиции Майка: "))
i = int(input("Инвестиции Ивана: "))

if (m > s) and (i > s):
    print("Оба вкладываются")
elif (m > s) and (i < s):
    print("Майк вкладывается")
elif (m < s) and (i > s):
    print("Иван вкладывается")
elif (m + i >= s):
    print("Вкладываются вместе")
else:
    print("Не хватает денег")