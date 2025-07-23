import random
def show_matrix(a):
    for i in a:
        print(*i)

#Функция для создания матрицы 10х10
# def gen_matrix():
#     return [[random.randint(-100, 100) for i in range(10)] for i in range(10)]

def gen_matrix():
    x = random.randint(2, 10)
    y = random.randint(2, 10)
    return [[random.randint(-100, 100) for i in range(x)] for i in range(y)]

def plus_matrix(mat1, mat2):
    x = max(len(mat1), len(mat2))
    y = max(len(mat1[0]), len(mat2[0]))
    # Код под матрицы 10х10
    # x = 10
    # y = 10
    # mat3 = []
    # for i in range(x):
    #     mat3_l = []
    #     for j in range(y):
    #         mat3_l.append(mat1[i][j]+mat2[i][j])
    #     mat3.append(mat3_l)
    mat3 = []
    for i in range(x):
        mat3_l = []
        z_mat1 = 0
        z_mat2 = 0
        for j in range(y):
            if i < len(mat1) and j < len(mat1[0]): 
                z_mat1 = mat1[i][j]
            else: z_mat1 = 0
            if i < len(mat2) and j < len(mat2[0]): 
                z_mat2 = mat2[i][j]
            else: z_mat2 = 0 
            mat3_l.append(z_mat1 + z_mat2)
        mat3.append(mat3_l)
    return mat3

m1 = gen_matrix()
m2 = gen_matrix()
print("Матрица 1")
show_matrix(m1)
print("\nМатрица 1")
show_matrix(m2)
print("\nРезультат сложения")
show_matrix(plus_matrix(m1, m2))