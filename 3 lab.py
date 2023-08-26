'''
Задание на матрицы №1

С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х
равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в
интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.
Каждая из матриц B,C,D,E имеет вид....

(ИСТбд-11)

Для простоты все индексы в подматрицах относительные. Библиотечными методами пользоваться нельзя.

Вариант 23
Формируется матрица F следующим образом: если в Е сумма чисел, больших К в нечетных столбцах
в области 3 больше, чем произведение чисел по периметру в области 2, то поменять в Е симметрично
области 1 и 2 местами, иначе С и В поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: (К * A) * F + K * Fт.
Выводятся по мере формирования А, F и все матричные операции последовательно.
'''



from random import randint
import copy

# ВВОД ДАННЫХ

print('Введите число N не меньше 6:', end = ' ')
n = int(int(input()))

if n < 6:
    print('Введённое число N некорректно')
    exit(0)

print('Введите число K:', end = ' ')
k = int(int(input()))


print()
print()


# ВЫВОД МАТРИЦЫ A

def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print('{:5d}'.format(j), end = ' ')
        print()
    print('\n')

A = [[randint(-10,10) for j in range(n)] for i in range(n)]

print('Матрица A')
print_matrix(A)
print()
print()


F = A


# ВЫВОД МАТРИЦЫ E

print('Матрица E')
for i in range(n // 2, n):
    for j in range(n // 2, n):
        print('{:5d}'.format(A[i][j]), end = ' ')
    print()
print()
print()


#СУММА ЧИСЕЛ В ОБЛАСТИ Е, БОЛЬШИХ К В НЕЧЕТНЫХ СТОЛБЦАХ В ОБЛАСТИ 3

sum_e_3 = 0


num_of_elements = n // 2 + n % 2
if (n // 2 + n % 2) % 2 == 1:
    current_i = (n // 2) + n // 4
    current_j = (n // 2) + n // 4
    dx = 1

else:
    current_i = (n // 2) + n // 4
    current_j = (n // 2) + n // 4
    if n % 2 == 0:
        current_i -= 1
    else:
        current_j += 1
    dx = 2


for i in range(current_j, n, 2):
    for j in range(current_i, current_i + dx):

        sum_e_3 += F[j][i] if F[j][i] > k else 0
    dx += 4
    current_i -= 2

print('Сумма чисел в области е, больших к в нечетных столбцах в области 3:', sum_e_3, end = ' ')
print()


#ПРОИЗВЕДЕНИЕ ЧИСЕЛ ПО ПЕРИМЕТРУ В ОБЛАСТИ 2

current_i = n // 2
current_j = n // 2

compos_e_2 = 1

if (n // 2 + n % 2) % 2 == 1:
    for j in range(n // 2 + 1, n - 1):
        compos_e_2 *= F[current_i][j]
        current_j += 1

    current_j += 1
    for i in range(num_of_elements // 2 + num_of_elements % 2 - 1):
        compos_e_2 *= F[current_i][current_j]
        current_j -= 1
        current_i += 1

    while current_i >= n // 2:
        compos_e_2 *= F[current_i][current_j]
        current_j -= 1
        current_i -= 1

else:
    for j in range(n // 2 + 1, n - 1):
        compos_e_2 *= F[current_i][j]
        current_j += 1

    current_j += 1
    for i in range(num_of_elements // 2 + num_of_elements % 2 - 1):
        compos_e_2 *= F[current_i][current_j]
        current_j -= 1
        current_i += 1
    compos_e_2 *= F[current_i][current_j]
    current_j -= 1
    compos_e_2 *= F[current_i][current_j]

    while current_i >= n // 2 + 1:
        current_j -= 1
        current_i -= 1

        compos_e_2 *= F[current_i][current_j]

print('Произведение чисел по периметру в области 2:', compos_e_2, end = ' ')
print()


#ФОРМИРОВАНИЕ МАТРИЦЫ F

if sum_e_3 > compos_e_2:
    current_i = n // 2
    current_j = n // 2
    for i in range(n // 2):
        for j in range(i, n //2 - i):
            F[i + n // 2][j + n // 2], F[j + n // 2][i + n // 2] = F[j + n // 2][i + n // 2], F[i + n // 2][j + n // 2]

else:
    for i in range(n // 2):
        for j in range(n // 2):
            F[i][j], F[i][j + n // 2] = F[i][j + n // 2], F[i][j]

print()
print()
print("Матрица E")
for i in range(n // 2, n):
    for j in range(n // 2, n):
        print('{:5d}'.format(A[i][j]), end = ' ')
    print()
print()


print('Матрица F')
print_matrix(F)


print()
print()


#ВЫЧИСЛЕНИЕ ВЫРАЖЕНИЯ: (К * A) * F + K * Fт

KA = []
KAF = []
Ftrans = []
KFtrans = []
KAFKFtrans = []

for i in range(n):
    KA.append([0]*n)
    KAF.append([0] * n)
    Ftrans.append([0] * n)
    KFtrans.append([0] * n)
    KAFKFtrans.append([0] * n)


print('Вычисление выражения: (К * A) * F + K * Fт')


print()
print()


print('K * A')
print()

for i in range(len(F)):
    for j in range(len(F)):
        KA[i][j] = (k * A[i][j])
        print('{:5d}'.format(KA[i][j]), end = '')
    print()
print()
print()


print('(K * A) * F')
print()

for i in range(len(F)):
   for j in range(len(F)):
       KAF[i][j] = KA[i][j] * F[i][j]
       print('{:5d}'.format(KAF[i][j]), end = ' ')
   print()
print()
print()


print('Fт')
print()

for i in range(len(F)):
    for j in range(len(F)):
        Ftrans[i][j] = F[j][i]
        print('{:5d}'.format(Ftrans[i][j]), end = ' ')
    print()
print()
print()


print('K * Fт')
print()

for i in range(len(F)):
    for j in range(len(F)):
        KFtrans[i][j] = k * F[j][i]
        print('{:5d}'.format(KFtrans[i][j]), end = ' ')
    print()
print()
print()


print('((K * A) * F) + (K * Fт)')
print()

for i in range(len(F)):
    for j in range(len(F)):
        KAFKFtrans[i][j] = KAF[i][j] + KFtrans[i][j]
        print('{:5d}'.format(KAFKFtrans[i][j]), end = ' ')
    print()
print()
print()