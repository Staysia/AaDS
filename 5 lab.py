#Задана рекуррентная функция. Область определения функции – натуральные числа.
#Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
#Определить границы применимости рекурсивного и итерационного подхода.
#Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
#23.F(1) = 1, F(2) = 1, F(n) = F(n-2)*(n-1) + 2, при n > 2

import time
import matplotlib.pyplot as plt

def rec(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return rec((n-2)*(n-1) + 2)

def iter(n):
    r = 1
    for i in range(2, n+1):
            r = r * ((n-2)*(n-1) + 2)
    return r

n = int(input("Введите число n: "))

start_time = time.time()
f_rec = F_rec(n)
end_time = time.time()
recursive_time = end_time - start_time

start_time = time.time()
f_iter = F_iter(n)
end_time = time.time()
iterative_time = end_time - start_time

print("F({}) = {} (рекурсивно в {:.6f} секунд)".format(n, f_rec, recursive_time))
print("F({}) = {} (итеративно в {:.6f} секунд)".format(n, f_iter, iterative_time))

plt.plot([n], [recursive_time], 'ro', label='Рекурсивно')
plt.plot([n], [iterative_time], 'bo', label='Итеративно')
plt.xlabel('n')
plt.ylabel('Время (с)')
plt.legend()
plt.show()
