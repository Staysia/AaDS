'''
Написать программу, которая читая файл, распознает, преобразует и выводит на экран числа по определенному правилу.
Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
Распознование делать через регулярные выражения. В вариантах, где есть параметр К, К заменяется на любое число.
Вариант 23.
Восьмиричные числа не превышающие 4096 10. Выводит на экран нечетные числа, содержащие четное количество цифр, превышающее К.
Список используемых цифр выводится отдельно.
'''

import re

print("введите k:", end=" ")
k = int(input())
print('')
print('числа, подходящие под условие задачи: ')
num = ''
kol_1 = 0
kol_2 = 0
slovar = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь'}

with open("text.txt",'r') as f:
    text = f.read()  # Читаем весь файл сразу
    if not text:
        print("файл пустой")
        kol_1 += 1
    else:
        # Находим все восьмеричные числа
        numbers = re.findall(r'\b[0-7]+\b', text)  # \b - граница слова
        i_z = set()
        for num in numbers:
            if (len(num) > k) and (len(num) % 2 == 0) and (int(num, 8) % 2 != 0) and (int(num, 8) <= 4096):
                kol_2 += 1
                print(num, end=' ')
                i_z.update(num)
                print(' ')
    if kol_2 == 0:
        print("чисел не найдено")
        
print('')
print("список используемых цифр: ", sorted(i_z))
