#Задана рекуррентная функция. Область определения функции – натуральные числа.
#Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить границы применимости рекурсивного и итерационного подхода.
#Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
#23.F(1) = 1, F(2) = 1, F(n) = F(n-2)*(n-1) + 2, при n > 2

import timeit
import matplotlib.pyplot as plt

a = []
b = []

def recF(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return recF(n-2) * (n-1) + 2

def iterf(n):
    if n == 1 or n == 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, n + 1):
            c = a * (n-1) + 2
            a = b
            b = c
        return b

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('№' + ' ' + 'Рекурсивно' +'Итеративно')
for i in nums:
    a.append(timeit.timeit(lambda: paf(i), number = 20000))
    b.append(timeit.timeit(lambda: pav(i), number = 20000))
    print(i, ' ', a[-1], '|', b[-1])
plt.xlabel('Числовые значения')
plt.ylabel('Время поиска')
plt.plot(nums, a, label='Рекурсивно')
plt.plot(nums, b, label='Итеративно')
plt.legend()
plt.show()
