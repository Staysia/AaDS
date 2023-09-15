'''
Задана рекуррентная функция. Область определения функции – натуральные числа.
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
Определить границы применимости рекурсивного и итерационного подхода.
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
23.F(1) = 1, F(2) = 1, F(n) = 'F(n-2)'*(n-1) + 2, при n > 2
'''


import timeit
import matplotlib.pyplot as plt

a = []
b = []

def f_rek(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return f_rek(n-2) * (n-1) + 2

def f_iter(n):
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


try:
    n = int(input('Введите натуральное число n: '))

    while n < 1:
        n = int(input("Введите натуральное число: "))

    start = timeit.default_timer()
    result = f_rek(n)
    print("\nРекурсия:", result, "\nВремя:", '{:.7f}'.format(timeit.default_timer() - start))

    start = timeit.default_timer()
    result = f_iter(n)
    print("\nИтерация:", result, "\nВремя:", '{:.7f}'.format(timeit.default_timer() - start))


    s = int(input("С каким шагом будет формироваться таблица? Введите число: "))

    rek_times = []
    iter_times = []
    rek_values = []
    iter_values = []
    n_values = list(range(1, n + 1,s))

    for n in n_values:
        start = timeit.default_timer()
        rek_values.append(f_rek(n))
        rek_times.append(timeit.default_timer() - start)

        start = timeit.default_timer()
        iter_values.append(f_iter(n))
        iter_times.append(timeit.default_timer() - start)

    t_data = []
    for i, n in enumerate(n_values):
        t_data.append([n, '{:.7f}'.format(rek_times[i]),'{:.7f}'.format(iter_times[i]), rek_values[i], iter_values[i]])
    print('{:<5}|{:<15}|{:<15}|{:<35}|{:<35}'.format('n', 'Время рекурсии','Время итерации','Значение рекурсии','Значение итерации'))
    for data in t_data:
        print('{:<5}|{:<15}|{:<15}|{:<35}|{:<35}'.format(data[0], data[1],data[2], data[3],data[4]))

    plt.plot(n_values, iter_times, label='Итерация')
    plt.plot(n_values, rek_times, label='Рекурсия')
    plt.xlabel('n')
    plt.ylabel('Время (с)')
    plt.title('Сравнение рекурсивного и итерационного подхода')
    plt.legend()
    plt.show()


except ValueError:
    print('Перезагрузите программу и введите натуральное число')
    
