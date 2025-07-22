d = int(input("Число: "))
ten = (d // 10) % 10
ten **= d % 10
ten *= (d // 100) % 10
ten /= ((d // 10000)-(d // 1000) % 10)
print(ten)