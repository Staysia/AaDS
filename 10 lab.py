from tkinter import *
from tkinter import messagebox
import random

# создание окна
window = Tk()
window.title('Крестики-Нолики')
window.resizable(False, False)

game_run = True # для запрета делать ходы после выявления победителя
field = [] # двумерный список, в котором хранятся кнопки игрового поля
cross_count = 0 # отслеживание количества крестиков на поле, по выставлению пятого - ничья

# начало новой игры - все кнопки пустые и белые
def new_game():
    for row in range(3): # строка
        for col in range(3): # столбец
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'white'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0

# проверка возможности хода
def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')

# проверка пободы
# smb - символ крестика или нолика
def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'light green'
        if a1['text'] == 'X' and a2['text'] == 'X' and a3['text'] == 'X':
            messagebox.showinfo("information", "Выиграл игрок Х")
        if a1['text'] == 'O' and a2['text'] == 'O' and a3['text'] == 'O':
            messagebox.showinfo("information", "Выиграл игрок O")
        global game_run
        game_run = False

# возможность выиграть
def can_win(a1,a2,a3,smb):
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

# наилучший ход компьютера
def computer_move():
    # проверка возможности победы
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    # проверка возможной победы противника за один ход
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    # если центр не занят, то занимает его
    if field[1][1]['text'] == ' ':
        field[1][1]['text'] = 'O'
        return
    # случайный ход
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break

# отрисовка игрового поля
for row in range(3):
    line = []
    for col in range(3):
        button = Button(window, text=' ', width=4, height=2,
                        font=('Times New Roman Bold', 32, 'bold'),
                        background='white',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(window, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

window.mainloop()