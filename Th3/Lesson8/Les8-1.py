n = int(input("Введите количество чисел: "))
a = []
b = []
for i in range(n): 
    a.append(int(input("Введите очередное число: ")))
a.reverse()
print(a)
