def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac

a = int(input("Введите число: "))
res = []
for k in range(factorial(a),0,-1):
    res.append(factorial(k))

print(res)