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
        for i in self.letters:
            print(i)

    def slovo_kol_2(self):
        for i1 in self.letters:
            for i2 in self.letters:
                print(i1 + i2)
                isEndsCons(i1 + i2)

    def slovo_kol_3(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.letters:
                    print(i1 + i2 + i3)
                    isEndsCons(i1 + i2 + i3)

    def slovo_kol_4(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.letters:
                        print(i1 + i2 + i3 + i4)
                        isEndsCons(i1 + i2 + i3 + i4)

    def slovo_kol_5(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.letters:
                            print(i1 + i2 + i3 + i4 + i5)
                            isEndsCons(i1 + i2 + i3 + i4 + i5)

    def slovo_kol_6(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.word:
                            for i6 in self.letters:
                                print(i1 + i2 + i3 + i4 + i5 + i6)
                                isEndsCons(i1 + i2 + i3 + i4 + i5 + i6)

    def slovo_kol_7(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.word:
                            for i6 in self.word:
                                for i7 in self.letters:
                                    print(i1 + i2 + i3 + i4 + i5 + i6 + i7)
                                    isEndsCons(i1 + i2 + i3 + i4 + i5 + i6 + i7)

    def slovo_kol_8(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.word:
                            for i6 in self.word:
                                for i7 in self.word:
                                    for i8 in self.letters:
                                        print(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)
                                        isEndsCons(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8)

    def slovo_kol_9(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.word:
                            for i6 in self.word:
                                for i7 in self.word:
                                    for i8 in self.word:
                                        for i9 in self.letters:
                                            print(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9)
                                            isEndsCons(i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9)

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
