import random
while True:
    try:
        n = int(input('Введите размер матрицы NxN: '))
        if n <= 0:
            print('Ошибка! Попробуйте еще раз.')
        else:
            break
    except Exception:
        print('Ошибка! Попробуйте еще раз.')

a = [[random.randint(-20,20) for i in range(n)] for j in range(n)]

print('Исходный список:')
for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()

s = 0
for i in range(n):
    for j in range(n-1-i):
        s += (a[i][j])
print('Сумма элементов выше побочной диагонали:',s)





# сумма элементов побочной диагонали
# s = 0
# for i in range(n):
#     s += (a[i][n-1-i])
# print(s)

