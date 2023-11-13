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


for i in letters:
    print(i)

for i1 in letters:
    for i2 in letters:
        print(i1 + i2)
        isEndsCons(i1 + i2)


for i1 in letters:
    for i2 in word:
        for i3 in letters:
            print(i1 + i2 + i3)
            isEndsCons(i1 + i2 + i3)

for i1 in letters:
    for i2 in word:
        for i3 in word:
            for i4 in letters:
                print(i1 + i2 + i3 + i4)
                isEndsCons(i1 + i2 + i3 + i4)


for i1 in letters:
    for i2 in word:
        for i3 in word:
            for i4 in word:
                for i5 in letters:
                    print(i1 + i2 + i3 + i4 + i5)
                    isEndsCons(i1 + i2 + i3 + i4 + i5)


for i1 in letters:
    for i2 in word:
        for i3 in word:
            for i4 in word:
                for i5 in word:
                    for i6 in letters:
                        print(i1 + i2 + i3 + i4 + i5 + i6)
                        isEndsCons(i1 + i2 + i3 + i4 + i5 + i6)


for i1 in letters:
    for i2 in word:
        for i3 in word:
            for i4 in word:
                for i5 in word:
                    for i6 in word:
                        for i7 in letters:
                            print(i1 + i2 + i3 + i4 + i5 + i6 + i7)
                            isEndsCons(i1 + i2 + i3 + i4 + i5 + i6 + i7)


for i1 in letters:
    for i2 in word:
        for i3 in word:
            for i4 in word:
                for i5 in word:
                    for i6 in word:
                        for i7 in word:
                            for i8 in letters:
                                print(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)
                                isEndsCons(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)

for i1 in letters:
    for i2 in word:
        for i3 in word:
            for i4 in word:
                for i5 in word:
                    for i6 in word:
                        for i7 in word:
                            for i8 in word:
                                for i9 in letters:
                                    print(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9)
                                    isEndsCons(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9)


print("Количество слов, которые начинаются и заканчиваются на согласные буквы:", count)
