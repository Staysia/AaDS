from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as mb
root = Tk()
root.title("Лабораторная работа №21")
root.geometry("400x400")
frame = Frame(root)
au_password = StringVar()
reg_password = StringVar()
au_login = StringVar()
reg_login = StringVar()
#bg = PhotoImage(file="backgrimage.png")
def entry_regist_and_login():
    canvas = Canvas(root, width=400, height=400)
    canvas.pack(fill="both", expand=True)
    #canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.create_text(200, 25, text='Регистрация', font='30', fill="#FFFFFF")
    canvas.create_text(200, 60, text='Введите логин')
    entry_login = Entry(root, textvariable=reg_login)
    entry_login = canvas.create_window(140, 70, anchor="nw", window=entry_login)
    canvas.create_text(200, 110, text='Введите пароль')
    entry_password = Entry(root, textvariable=reg_password, show='*')
    entry_password = canvas.create_window(140, 120, anchor="nw", window=entry_password)
    button_a = Button(root, text='Зарегистрироваться', command=reg_login_and_password_error, bg='#FFFFFF')
    button_a = canvas.create_window(140, 160, anchor="nw", window=button_a)
    canvas.create_text(200, 215, text='Авторизация', font='30', fill="#FFFFFF")
    canvas.create_text(200, 250, text='Введите логин')
    entry_login = Entry(root, textvariable=au_login)
    entry_login = canvas.create_window(140, 260, anchor="nw", window=entry_login)
    canvas.create_text(200, 300, text='Введите пароль')
    entry_password = Entry(root, textvariable=au_password, show='*')
    entry_password = canvas.create_window(140, 310, anchor="nw", window=entry_password)
    button_r = Button(root, text='Авторизироваться', command=au_login_and_password_error, bg='#FFFFFF')
    button_r = canvas.create_window(145, 350, anchor="nw", window=button_r)
def au_login_and_password_error():
    if (len(au_login.get()) == 0 or len(au_password.get()) == 0) or (
            len(au_login.get()) == 0 and len(au_password.get()) == 0) or au_login.get().count(' ') > 0 or \
            au_password.get().count(' ') > 0:
        mb.showerror("Ошибка", "Должны быть введены данные")
    else:
        file = open('reg_login.txt', 'r')
        while TRUE:
            line = file.readline()
            line = line.split()
            if len(line) == 0:
                file.close()
                mb.showerror("Ошибка", "Неверные логин или пароль")
                break
            elif line[0] == au_login.get() and line[1] == au_password.get():
                file.close()
                root.destroy()
                window = Tk()
                window.title("Успешная авторизация")
                window.geometry("400x400")
                canvas = Canvas(window, width=400, height=400)
                canvas.pack(fill="both", expand=True)
                '''img = PhotoImage(file="bckgrimg.png")
                image = canvas.create_image(200, 200, image = img)'''
                canvas.create_text(200, 200, text='Вы успешно авторизированы!', font='30')
                def window_destroy():
                    window.destroy()
                button_w = Button(window, text='Начать игру', command=window_destroy, bg='#FFFFFF')
                button_w = canvas.create_window(200, 250, window=button_w)
                window.grab_set()
                window.mainloop()
                break
def reg_login_and_password_error():
    if (len(reg_login.get()) == 0 or len(reg_password.get()) == 0) or (
            len(reg_login.get()) == 0 and len(reg_password.get()) == 0) or reg_login.get().count(' ') > 0 or \
            reg_password.get().count(' ') > 0:
        mb.showerror("Ошибка", "Должны быть введены данные")
    else:
        file = open('reg_login.txt', 'a')
        file.write(reg_login.get() + ' ' + reg_password.get() + '\n')
        file.close()
        mb.showinfo("Успешная регистрация", "Вы успешно зарегистрировались. Пожалуйста, авторизуйтесь")
entry_regist_and_login()
root.resizable(width=False, height=False)
root.mainloop()