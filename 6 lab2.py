'''
Вариант 23. Составьте все различные лексемы из букв слова «компьютер» по законам русского языка.
2 часть – составленные лексемы начинаются и заканчиваются на согласные буквы, вывести их количество.
'''


word = "компьютер"
letters = "кмптр"
count = 0

def isEndsCons(word):
    global count
    if word[0] in letters and word[-1] in letters:
        count += 1


for i in range(len(word)):
    if word[i] in letters:
        print(word[i])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        if (word[i1] in letters) + (word[i2] in letters) == 2:
            print(word[i1] + word[i2])
            isEndsCons(word[i1] + word[i2])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            if (word[i1] in letters) + (word[i2] in word) + (word[i3] in letters) == 3:
                print(word[i1] + word[i2] + word[i3])
                isEndsCons(word[i1] + word[i2] + word[i3])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                if (word[i1] in letters) + (word[i2] in word) + (word[i3] in word) + (word[i4] in letters) == 4:
                    print(word[i1] + word[i2] + word[i3] + word[i4])
                    isEndsCons(word[i1] + word[i2] + word[i3] + word[i4])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    if (word[i1] in letters) + (word[i2] in word) + (word[i3] in word) + (word[i4] in word) + (word[i5] in letters) == 5:
                        print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5])
                        isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        if (word[i1] in letters) + (word[i2] in word) + (word[i3] in word) + (word[i4] in word) + (word[i5] in word) + (word[i6] in letters) == 6:
                            print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6])
                            isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        for i7 in range(len(word)):
                            if (word[i1] in letters) + (word[i2] in word) + (word[i3] in word) + (word[i4] in word) + (word[i5] in word) + (word[i6] in word) + (word[i7] in letters) == 7:
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
                                if (word[i1] in letters) + (word[i2] in word) + (word[i3] in word) + (word[i4] in word) + (word[i5] in word) + (word[i6] in word) + (word[i7] in word) + (word[i8] in letters) == 8:
                                    print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8])
                                    isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        for i7 in range(len(word)):
                            for i8 in range(len(word)):
                                for i9 in range(len(word)):
                                    if (word[i1] in letters) + (word[i2] in word) + (word[i3] in word) + (word[i4] in word) + (word[i5] in word) + (word[i6] in word) + (word[i7] in word) + (word[i8] in word) + (word[i9] in letters) == 9:
                                        print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8] + word[i9])
                                        isEndsCons(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8] + word[i9])


print("Количество слов, которые начинаются и заканчиваются на согласные буквы:", count)
