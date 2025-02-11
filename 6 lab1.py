'''
Вариант 23. Составьте все различные лексемы из букв слова «компьютер» по законам русского языка.
1 часть – написать программу в соответствии со своим вариантом задания.
'''


word = "компьютер"
for i in range(len(word)):
    print(word[i])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        if i1 != i2:
            print(word[i1] + word[i2])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            if i1 != i2 and i2 != i3:
                print(word[i1] + word[i2] + word[i3])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                if i1 != i2 and i2 != i3 and i3 != i4:
                    print(word[i1] + word[i2] + word[i3] + word[i4])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5:
                        print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6:
                            print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        for i7 in range(len(word)):
                            if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6 and i6 != i7:
                                print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7])


for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        for i7 in range(len(word)):
                            for i8 in range(len(word)):
                                if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6 and i6 != i7 and i7 != i8:
                                    print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8])

for i1 in range(len(word)):
    for i2 in range(len(word)):
        for i3 in range(len(word)):
            for i4 in range(len(word)):
                for i5 in range(len(word)):
                    for i6 in range(len(word)):
                        for i7 in range(len(word)):
                            for i8 in range(len(word)):
                                for i9 in range(len(word)):
                                    if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6 and i6 != i7 and i7 != i8 and i8 != i9:
                                        print(word[i1] + word[i2] + word[i3] + word[i4] + word[i5] + word[i6] + word[i7] + word[i8] + word[i9])
