import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class ComputerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Комбинации букв из слова 'компьютер'")

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
        if word[0] in self.computer.letters and word[-1] in self.computer.letters:
            self.count += 1
            return True  # Indicate match for additional features
        return False

    def display_len1(self):
        self.text_area.delete("1.0", tk.END)
        output = "\n".join(self.computer.letters)
        self.text_area.insert(tk.END, output)
        self.count = 0 # Сбрасываем счетчик. Считаем он нам не нужен для данного случая

    def display_len2(self):
        self.display_combinations(self.computer.slovo_kol_2_generator(), 2)

    def display_len3(self):
         self.display_combinations(self.computer.slovo_kol_3_generator(), 3)

    def display_len4(self):
        self.display_combinations(self.computer.slovo_kol_4_generator(), 4)

    def display_len5(self):
        self.display_combinations(self.computer.slovo_kol_5_generator(), 5)

    def display_len6(self):
        self.display_combinations(self.computer.slovo_kol_6_generator(), 6)

    def display_len7(self):
        self.display_combinations(self.computer.slovo_kol_7_generator(), 7)

    def display_len8(self):
        self.display_combinations(self.computer.slovo_kol_8_generator(), 8)

    def display_len9(self):
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