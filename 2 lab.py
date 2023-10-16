'''
Вариант 23.
Восьмиричные числа не превышающие 409610. Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр выводится отдельно.
'''

import re

file = open("text.txt", 'r')
a = '' #строка из файла
num = [] #цифр выводим отдельно прописью
k = int(input())
while True:
    a = file.readline() #читаем строку из файла
    if a == '':
        break
    res_a = (re.findall('[\d]*[\d]{%s}[1357]'%2, a))
    if len(res_a) > 0:
            for i in range(len(res_a)):
                if a != ' ' and a != ',' and a != '.' and a != '"':
                    if len(res_a[i]) % 2 == 0 and len(res_a[i]) > k:
                        print(res_a[i])
                        for j in range(len(res_a[i])):
                            if not ((res_a[i])[j] in num):
                                num.append((res_a[i])[j])
print(*sorted(num)) #Список используемых цифр
