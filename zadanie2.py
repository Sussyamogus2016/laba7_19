import random
def inp():
    while True:
        try:
            n = int(input())
            if n <= 0:
                print('Ошибка! Попробуйте еще раз.')
            else:
                break
        except Exception:
            print('Ошибка! Попробуйте еще раз.')
    return n

print('Введите n: ', end = '')
n = inp()
print('Введите m: ', end = '')
m = inp()

a = [[random.randint(-20,20) for i in range(n)] for j in range(m)]

print(a)
print('Исходный список')
for i in range(m):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()

# c = 0
# for j in range(m+1):
#     flag = 0
#     for i in range(n-1):
#         if a[i][j] == 0:
#             flag = 1
#             break
#     if flag == 0:
#         c += 1
# print('Кол-во столбцов, не содержащих нулевых элементов:', c)

stolb = 0
el = []
c = 0
while stolb <= n-1:
    for i in a:
        el.append(i[stolb])
    flag = 0
    for i in el:
        if i == 0:
            flag = 1
    if flag == 0:
        c += 1
    el = []
    stolb += 1
print(c)

