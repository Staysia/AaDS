'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
В программе должны быть реализованы минимум один класс, три атрибута, два метода

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

class Computer:
    def __init__(self):
        self.word = "компьютер"
        self.letters = "кмптр"

    def slovo_kol_1(self):
        for i in range(len(self.word)):
            if self.word[i] in self.letters:
                print(self.word[i])

    def slovo_kol_2(self):
        for i1 in range(len(self.word)):
            for i2 in range(len(self.word)):
                if (self.word[i1] in self.letters) + (self.word[i2] in self.letters) == 2:
                    print(self.word[i1] + self.word[i2])
                    isEndsCons(self.word[i1] + self.word[i2])

    def slovo_kol_3(self):
        for i1 in range(len(self.word)):
            for i2 in range(len(self.word)):
                for i3 in range(len(self.word)):
                    if (self.word[i1] in self.letters) + (self.word[i2] in self.word) + (self.word[i3] in self.letters) == 3:
                        print(self.word[i1] + self.word[i2] + self.word[i3])
                        isEndsCons(self.word[i1] + self.word[i2] + self.word[i3])

    def slovo_kol_4(self):
        for i1 in range(len(self.word)):
            for i2 in range(len(self.word)):
                for i3 in range(len(self.word)):
                    for i4 in range(len(self.word)):
                        if (self.word[i1] in self.letters) + (self.word[i2] in self.word) + (self.word[i3] in self.word) + (self.word[i4] in self.letters) == 4:
                            print(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4])
                            isEndsCons(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4])

    def slovo_kol_5(self):
        for i1 in range(len(self.word)):
            for i2 in range(len(self.word)):
                for i3 in range(len(self.word)):
                    for i4 in range(len(self.word)):
                        for i5 in range(len(self.word)):
                            if (self.word[i1] in self.letters) + (self.word[i2] in self.word) + (self.word[i3] in self.word) + (self.word[i4] in self.word) + (self.word[i5] in self.letters) == 5:
                                print(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5])
                                isEndsCons(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5])

    def slovo_kol_6(self):
        for i1 in range(len(self.word)):
            for i2 in range(len(self.word)):
                for i3 in range(len(self.word)):
                    for i4 in range(len(self.word)):
                        for i5 in range(len(self.word)):
                            for i6 in range(len(self.word)):
                                if (self.word[i1] in self.letters) + (self.word[i2] in self.word) + (self.word[i3] in self.word) + (self.word[i4] in self.word) + (self.word[i5] in self.word) + (self.word[i6] in self.letters) == 6:
                                    print(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5] + self.word[i6])
                                    isEndsCons(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5] + self.word[i6])

    def slovo_kol_7(self):
        for i1 in range(len(self.word)):
            for i2 in range(len(self.word)):
                for i3 in range(len(self.word)):
                    for i4 in range(len(self.word)):
                        for i5 in range(len(self.word)):
                            for i6 in range(len(self.word)):
                                for i7 in range(len(self.word)):
                                    if (self.word[i1] in self.letters) + (self.word[i2] in self.word) + (self.word[i3] in self.word) + (self.word[i4] in self.word) + (self.word[i5] in self.word) + (self.word[i6] in self.word) + (self.word[i7] in self.letters) == 7:
                                        print(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5] + self.word[i6] + self.word[i7])
                                        isEndsCons(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5] + self.word[i6] + self.word[i7])

    def slovo_kol_8(self):
        for i1 in range(len(self.word)):
            for i2 in range(len(self.word)):
                for i3 in range(len(self.word)):
                    for i4 in range(len(self.word)):
                        for i5 in range(len(self.word)):
                            for i6 in range(len(self.word)):
                                for i7 in range(len(self.word)):
                                    for i8 in range(len(self.word)):
                                        if (self.word[i1] in self.letters) + (self.word[i2] in self.word) + (self.word[i3] in self.word) + (self.word[i4] in self.word) + (self.word[i5] in self.word) + (self.word[i6] in self.word) + (self.word[i7] in self.word) + (self.word[i8] in self.letters) == 8:
                                            print(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5] + self.word[i6] + self.word[i7] + self.word[i8])
                                            isEndsCons(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5] + self.word[i6] + self.word[i7] + self.word[i8])

    def slovo_kol_9(self):
        for i1 in range(len(self.word)):
            for i2 in range(len(self.word)):
                for i3 in range(len(self.word)):
                    for i4 in range(len(self.word)):
                        for i5 in range(len(self.word)):
                            for i6 in range(len(self.word)):
                                for i7 in range(len(self.word)):
                                    for i8 in range(len(self.word)):
                                        for i9 in range(len(self.word)):
                                            if (self.word[i1] in self.letters) + (self.word[i2] in self.word) + (self.word[i3] in self.word) + (self.word[i4] in self.word) + (self.word[i5] in self.word) + (self.word[i6] in self.word) + (self.word[i7] in self.word) + (self.word[i8] in self.word) + (self.word[i9] in self.letters) == 9:
                                                print(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5] + self.word[i6] + self.word[i7] + self.word[i8] + self.word[i9])
                                                isEndsCons(self.word[i1] + self.word[i2] + self.word[i3] + self.word[i4] + self.word[i5] + self.word[i6] + self.word[i7] + self.word[i8] + self.word[i9])

c = Computer()
c.slovo_kol_1()
c.slovo_kol_2()
c.slovo_kol_3()
c.slovo_kol_4()
c.slovo_kol_5()
c.slovo_kol_6()
c.slovo_kol_7()
c.slovo_kol_8()
c.slovo_kol_9()

print("Количество слов, которые начинаются и заканчиваются на согласные буквы:", count)
