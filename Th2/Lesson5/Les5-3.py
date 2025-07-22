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