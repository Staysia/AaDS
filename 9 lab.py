from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Авторизация')
window.geometry('400x300')
window.resizable(False, False)

def check():
    data_login = entry_login.get()
    data_password = entry_password.get()
    if data_login == '':
        messagebox.showinfo('Информационное окно', 'Ошибка! Пустое поле! Введите логин!')
    if data_password == '':
        messagebox.showinfo('Информационное окно', 'Ошибка! Пустое поле! Введите пароль!')
    if data_login != '' and data_password != '':
        window.destroy()
        #Игровое окно
        second_window = Tk()
        second_window.title("Игра")
        second_window.geometry("600x600")
        second_window.resizable(False, False)
        #Информационное окно
        root = Toplevel()
        root.title('Информационное окно')
        root.geometry('400x300')
        root.resizable(False, False)
        root.attributes("-topmost", True)
        label_success = Label(root, text='Поздравляем! Вы успешно вошли!')
        label_success.pack(pady=80)
        def root_destroy():
            root.destroy()
        button_start = Button(root, text='Начать игру', command=root_destroy)
        button_start.pack(pady=20)
        
def showpass():
    if entry_password['show'] == '*':
        entry_password['show'] = ''
    else:
        entry_password['show'] = '*'

label_1 = Label(window, text='Введите логин:').pack(pady=20)
entry_login = Entry(window, width=50)
entry_login.pack()

label_2 = Label(window, text='Введите пароль:').pack(pady=20)
entry_password = Entry(window, width=50, show='*')
entry_password.pack()
button_1 = Button(window, text='Посмотреть пароль', command=showpass).pack(pady=10)

button_2 = Button(window, text='Войти', command=check).pack(pady=20)

window.mainloop()
