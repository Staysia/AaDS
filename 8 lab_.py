'''
Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации (л.р. №7) разработать
реализацию с использованием графического интерфейса. Допускается использовать любую графическую библиотеку питона.  Рекомендуется использовать
внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.
'''



import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class ComputerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Комбинации букв из слова 'компьютер'")

        # текстовое поле
        self.input_label = ttk.Label(master, text="Поиск лексем из букв слова «компьютер»", font='Arial 12')
        self.input_label.pack(anchor="n")
        self.input_label = ttk.Label(master, text="Cоставленные лексемы начинаются и заканчиваются на согласные буквы",
                                     font='Arial 12')
        self.input_label.pack(anchor="n")

        self.input_label = ttk.Label(master, text="Введите слово 'компьютер' или любое другое слово, количество букв которого не привышает 9: ", font='Arial 12')
        self.input_label.pack(anchor="n", pady=8)

        #окна ввода
        self.word_label = ttk.Label(master, text="Введите слово:")
        self.word_label.pack(pady=5)

        self.word_entry = ttk.Entry(master)
        self.word_entry.pack(pady=5)
        self.word_entry.insert(0, "компьютер")  # Значение по умолчанию

        # Label и Entry для ввода букв
        self.letters_label = ttk.Label(master, text="Введите буквы с которых будут начинаться и заканчиваться лексемы:")
        self.letters_label.pack(pady=5)

        self.letters_entry = ttk.Entry(master)
        self.letters_entry.pack(pady=5)
        self.letters_entry.insert(0, "кмптр")  # Значение по умолчанию

        self.computer = Computer()
        self.count = 0

        # Кнопки для генерации комбинаций
        self.button_len1 = ttk.Button(master, text="Комбинации длины 1", command=self.display_len1)
        self.button_len1.pack(pady=5)

        self.button_len2 = ttk.Button(master, text="Комбинации длины 2 (начинаются и заканчиваются согласными)", command=self.display_len2)
        self.button_len2.pack(pady=5)

        self.button_len3 = ttk.Button(master, text="Комбинации длины 3 (начинаются и заканчиваются согласными)", command=self.display_len3)
        self.button_len3.pack(pady=5)

        self.button_len4 = ttk.Button(master, text="Комбинации длины 4 (начинаются и заканчиваются согласными)", command=self.display_len4)
        self.button_len4.pack(pady=5)

        self.button_len5 = ttk.Button(master, text="Комбинации длины 5 (начинаются и заканчиваются согласными)", command=self.display_len5)
        self.button_len5.pack(pady=5)

        self.button_len6 = ttk.Button(master, text="Комбинации длины 6 (начинаются и заканчиваются согласными)", command=self.display_len6)
        self.button_len6.pack(pady=5)

        self.button_len7 = ttk.Button(master, text="Комбинации длины 7 (начинаются и заканчиваются согласными)", command=self.display_len7)
        self.button_len7.pack(pady=5)

        self.button_len8 = ttk.Button(master, text="Комбинации длины 8 (начинаются и заканчиваются согласными)", command=self.display_len8)
        self.button_len8.pack(pady=5)

        self.button_len9 = ttk.Button(master, text="Комбинации длины 9 (начинаются и заканчиваются согласными)", command=self.display_len9)
        self.button_len9.pack(pady=5)

        # Label для отображения количества комбинаций
        self.count_label = ttk.Label(master, text="Количество комбинаций, начинающихся и заканчивающихся согласными: 0")
        self.count_label.pack(pady=5)

        # Text area для вывода результатов
        self.text_area = scrolledtext.Text(master, height=2000, width=100)
        self.text_area.pack(pady=10)

    def isEndsCons(self, word):
        letters = self.letters_entry.get()
        if word and word[0] in letters and word[-1] in letters:  # Added word check
            self.count += 1
            return True
        return False

    def display_len1(self):
        self.update_word_and_letters()
        self.text_area.delete("1.0", tk.END)
        output = "\n".join(self.computer.letters)
        self.text_area.insert(tk.END, output)
        self.count = 0 # Сбрасываем счетчик. Считаем он нам не нужен для данного случая

    def display_len2(self):
        self.update_word_and_letters()
        self.display_combinations(self.computer.slovo_kol_2_generator(), 2)

    def display_len3(self):
        self.update_word_and_letters()
        self.display_combinations(self.computer.slovo_kol_3_generator(), 3)

    def display_len4(self):
        self.update_word_and_letters()
        self.display_combinations(self.computer.slovo_kol_4_generator(), 4)

    def display_len5(self):
        self.update_word_and_letters()
        self.display_combinations(self.computer.slovo_kol_5_generator(), 5)

    def display_len6(self):
        self.update_word_and_letters()
        self.display_combinations(self.computer.slovo_kol_6_generator(), 6)

    def display_len7(self):
        self.update_word_and_letters()
        self.display_combinations(self.computer.slovo_kol_7_generator(), 7)

    def display_len8(self):
        self.update_word_and_letters()
        self.display_combinations(self.computer.slovo_kol_8_generator(), 8)

    def display_len9(self):
        self.update_word_and_letters()
        self.display_combinations(self.computer.slovo_kol_9_generator(), 9)

    def display_combinations(self, combination_generator, length):
        self.text_area.delete("1.0", tk.END)
        self.count = 0
        output = ""
        for comb in combination_generator:
           output += comb + "\n"
           self.isEndsCons(comb)
        self.text_area.insert(tk.END, output)
        self.count_label.config(text=f"Количество комбинаций длины {length}, начинающихся и заканчивающихся согласными: {self.count}")

    def update_word_and_letters(self):
        word = self.word_entry.get()
        letters = self.letters_entry.get()
        self.computer.word = word
        self.computer.letters = letters

class Computer:
    def __init__(self):
        self.word = "компьютер"
        self.letters = "кмптр"
        self.all_letters = set(self.letters)

    def slovo_kol_2_generator(self):
        for i1 in self.letters:
            for i2 in self.letters:
                if i1 != i2:
                    yield i1 + i2

    def slovo_kol_3_generator(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.letters:
                    if i1 != i2 and i2 != i3:
                       yield i1 + i2 + i3

    def slovo_kol_4_generator(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.letters:
                        if i1 != i2 and i2 != i3 and i3 != i4:
                            yield i1 + i2 + i3 + i4

    def slovo_kol_5_generator(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.letters:
                            if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5:
                                yield i1 + i2 + i3 + i4 + i5

    def slovo_kol_6_generator(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.word:
                            for i6 in self.letters:
                                if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6:
                                    yield i1 + i2 + i3 + i4 + i5 + i6

    def slovo_kol_7_generator(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.word:
                            for i6 in self.word:
                                for i7 in self.letters:
                                    if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6 and i6 != i7:
                                        yield i1 + i2 + i3 + i4 + i5 + i6 + i7

    def slovo_kol_8_generator(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.word:
                            for i6 in self.word:
                                for i7 in self.word:
                                    for i8 in self.letters:
                                        if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6 and i6 != i7 and i7 != i8:
                                            yield i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8

    def slovo_kol_9_generator(self):
        for i1 in self.letters:
            for i2 in self.word:
                for i3 in self.word:
                    for i4 in self.word:
                        for i5 in self.word:
                            for i6 in self.word:
                                for i7 in self.word:
                                    for i8 in self.word:
                                        for i9 in self.letters:
                                            if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6 and i6 != i7 and i7 != i8 and i8 != i9:
                                                yield i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9


root = tk.Tk()
gui = ComputerGUI(root)
root.mainloop()
