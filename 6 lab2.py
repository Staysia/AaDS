'''
Вариант 23. Составьте все различные лексемы из букв слова «компьютер» по законам русского языка.
2 часть – согласные буквы не могут повторяться. Вывести количество составленных лексем, начинающихся и заканчивающихся на согласные буквы.
'''


word = "компьютер"
letters = "кмптр"
count = 0

def isEndsCons(word):
    global count
    if word[0] in letters and word[-1] in letters:
        count += 1


for i in range(len(word)):
    print(word[i])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        if word[i1] != word[i2]:
            print(word[i1] + word[i2])
            isEndsCons(word[i1] + word[i2])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            if len(set([word[i1], word[i2], word[i3]])) == 3:
                print(word[i1] + word[i2] + word[i3])
                isEndsCons(word[i1] + word[i2] + word[i3])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                if len(set([word[i1], word[i2], word[i3], word[i4]])) == 4:

                    print(word[i1] + word[i2] + word[i3] + word[i4])
                    isEndsCons(word[i1] + word[i2] + word[i3] + word[i4])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    if len(set([word[i1], word[i2], word[i3], word[i4], word[i5]])) == 5:
                        print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5])
                        isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        if len(set([word[i1], word[i2], word[i3], word[i4], word[i5], word[i6]])) == 6:
                            print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6])
                            isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        for i7 in range(len(word)):
                            if len(set([word[i1], word[i2], word[i3], word[i4], word[i5], word[i6], word[i7]])) == 7:
                                print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7])
                                isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        for i7 in range(len(word)):
                            for i8 in range(len(word)):
                                if len(set([word[i1], word[i2], word[i3], word[i4], word[i5], word[i6], word[i7], word[i8]])) == 8:
                                    print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8])
                                    isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[
                                        i8])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        for i7 in range(len(word)):
                            for i8 in range(len(word)):
                                for i9 in range(len(word)):
                                    if len(set([word[i1], word[i2], word[i3], word[i4], word[i5], word[i6], word[i7],
                                            word[i8], word[i9]])) == 9:
                                        print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8] + word[i9])

                                        isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8] + word[i9])


print("Количество слов, которые начинаются и заканчиваются на согласные буквы:", count)
