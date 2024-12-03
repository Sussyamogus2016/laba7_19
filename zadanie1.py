import random
# while True:
#     try:
#         n = int(input('Введите размер матрицы NxN: '))
#         if n > 0:
#             break
#     except Exception:
#         print('Ошибка! Попробуйте еще раз.')
n = 3
a = [[random.randint(-20,20) for i in range(n)] for j in range(n)]

print('Исходный список')
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()

s = 0
for i in range(n):
    s += (a[i][n-1-i])
print(s)

