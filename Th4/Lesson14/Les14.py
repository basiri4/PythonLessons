# def func(a, b, c = 8):
#     return a + b + c

# d = func(3,4);
# print(d)
def tmp(a, i = 0):
    if i < len(a): 
        print(a[i])
        tmp(a, i + 1)
    else:
        print("Конец списка")
        return
    

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

tmp(my_list)

