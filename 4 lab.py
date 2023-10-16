'''
Задание на матрицы №2

С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное
заполнение, а целенаправленное. Вид матрицы А: ИСТбд-11

Для простоты все индексы в подматрицах относительные.

По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.

Программа должна использовать функции библиотек numpy  и mathplotlib

Вариант 23
Формируется матрица F следующим образом: скопировать в нее А и  если в Е сумма чисел, больших К в нечетных
столбцах больше, чем произведение чисел по периметру, то поменять местами С и Е симметрично, иначе С и В
поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше
суммы диагональных элементов матрицы F, то вычисляется выражение: A*A-1 – K * F-1, иначе вычисляется выражение
(AТ +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.  Выводятся по мере формирования А,
F и все матричные операции последовательно.
'''



import matplotlib.pyplot as plt
import numpy as np

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print("%5d" % j, end=' ')
        print()
    print('\n')

print("Число n больше 6:", end='')
n = int(input())
print("Введите число k:", end='')
k = int(input())
A = np.random.randint(-10,10, (n,n))
numbers = [0] * 22
znak = [0, 0]
elements = [el for el in range(-10, 11)]


for i in range(n):
    for j in range(n):
        numbers[A[i][j]] += 1
        if A[i][j] < 0:
            znak[0] += 1
        else:
            znak[1] += 1
numbers = numbers[:-1]

print_matrix(A)
F = np.copy(A)


print("Матрица E")
for i in range(n // 2, n):
    for j in range(n // 2, n):
        print("%5d" % A[i][j], end=' ')
    print()


#сумма в 3 области
sum_e_3 = 0

num_of_elements = n // 2 + n % 2
current_i = (n // 2)
current_j = (n // 2)

for i in range(current_j, n, 2):
    for j in range(current_i, n):
        sum_e_3 += F[j][i] if F[j][i] > k else 0

#произведение по периметру
current_i = n // 2
current_j = n // 2
compos_e_2 = 1

for j in range(n // 2 + 1, n):
    compos_e_2 *= F[current_i][current_j]
    current_j += 1

for i in range(n // 2, n - 1):
    compos_e_2 *= F[current_i][current_j]
    current_i += 1

for i in range(n, n // 2 + 1, -1):
    compos_e_2 *= F[current_i][current_j]
    current_j -= 1

for i in range(n, n // 2, -1):
    compos_e_2 *= F[current_i][current_j]
    current_i -= 1


print(sum_e_3)
print(compos_e_2)


if sum_e_3 > compos_e_2:
    for i in range(n // 2):
        for j in range(n // 2):
            F[i][j], F[n - 1 - i][j] = F[n - 1 - i][j],  F[i][j]
else:
    for i in range(n // 2):
        for j in range(n // 2):
            F[i][j], F[i][j + n // 2] = F[i][j + n // 2], F[i][j]


print('Матрица F')
print(F)

#определители
o = np.linalg.det(F)
print('linalg:', int(o))

#диагональ
d = np.asarray(F)
print('Diagonal (sum): ', np.trace(d))

#транспонированные матрицы
t_A = np.transpose(A)
print('transpose A:', t_A)

t_F = np.transpose(F)
print('transpose F:', t_F)

#обратные матрицы
a = np.linalg.inv(A)
print('linalg.inv A:', a)

f = np.linalg.inv(F)
print('linalg.inv F:', f)

# нижняя треугольная матрица
G = np.tril(A)
print('G', G)


if int(o) > np.trace(d):
    d_1 = np.dot(A, a)
    print(d_1)
    d_2 = np.dot(k, f)
    print(d_2)
    d_3 = d_1 - d_2
    print('результат:', d_3)
else:
    D_1_1 = t_A + G
    print(D_1_1)
    D_1_2 = D_1_1 - t_F
    print(D_1_2)
    D_2 = np.dot(D_1_2, k)
    print(D_2)


plt.figure(figsize=(12, 7))

plt.subplot(2, 2, 1)
plt.bar(elements, numbers, label='Встречаемость в матрице')
plt.xlabel('Числа')
plt.ylabel('Частота')
plt.title('Пример столбчатой диаграммы')
plt.legend()


plt.subplot(2, 2, 2)
plt.pie(numbers, labels=elements)
plt.title("Пример круговой диаграммы")



plt.subplot(2, 2, 3)
plt.imshow(F,)

plt.subplot(2, 2, 4)
plt.plot(numbers, '--')

plt.show()
