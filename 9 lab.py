from tkinter import *
from tkinter import messagebox

def game():
    global game_window
    game_window = Tk()
    game_window.title("Игра")
    game_window.geometry("600x600")
    game_window.resizable(False, False)

def check_registration():
    check_login = entry_username_r.get()
    check_password = entry_password_r.get()
    if (check_login == '') or (check_password == '') or ((check_login == '') and (check_password == '')):
        messagebox.showerror('Информационное окно', 'Ошибка! Заполните пустое поле / пустые поля!')
    else:
        file = open('login.txt', 'w')
        file.write(entry_username_r.get() + ' ' + entry_password_r.get() + '\n')
        file.close()

        global inf_window
        inf_window = Tk()
        inf_window.title('Информационное окно')
        inf_window.geometry("350x115")
        inf_window.resizable(False, False)

        lable_inf_1 = Label(inf_window, text='Поздравляем! Вы успешно прошли регестрацию!')
        lable_inf_1.pack(ipady=10)
        lable_inf_2 = Label(inf_window, text='Для начала игры войдите в аккаунт.')
        lable_inf_2.pack()

        def inf_window_destroy():
            inf_window.destroy()

        def registration_window_destroy():
            registration_window.destroy()

        button_inf = Button(inf_window, text='Ок', command=lambda: [inf_window_destroy(), registration_window_destroy(), main_account_screen()])
        button_inf.pack(pady=10)

def registration():
    global registration_window
    registration_window = Tk()
    registration_window.title('Регестрация')
    registration_window.geometry("400x300")
    registration_window.resizable(False, False)

    global username_r
    global password_r
    global entry_username_r
    global entry_password_r
    username_r = StringVar()
    password_r = StringVar()

    lable_username_r = Label(registration_window, text='Придумайте логин:')
    lable_username_r.pack(pady=20)
    entry_username_r = Entry(registration_window, width=50)
    entry_username_r.pack()

    def showpass_r():
        if entry_password_r['show'] == '*':
            entry_password_r['show'] = ''
        else:
            entry_password_r['show'] = '*'

    lable_password_r = Label(registration_window, text='Придумайте пароль:')
    lable_password_r.pack(pady=20)
    entry_password_r = Entry(registration_window, width=50, show='*')
    entry_password_r.pack()

    button_password_r = Button(registration_window, text='Посмотреть пароль', command=showpass_r)
    button_password_r.pack(pady=10)

    button_register = Button(registration_window, text='Зарегестрироваьтся', command=check_registration)
    button_register.pack(pady=10)

def check_log_in():
    check_login_1 = entry_username.get()
    check_password_1 = entry_password.get()
    if (check_login_1 == '') or (check_password_1 == '') or ((check_login_1 == '') and (check_password_1 == '')):
        messagebox.showerror('Информационное окно', 'Ошибка! Заполните пустое поле / пустые поля!')
    else:
        file = open('login.txt', 'r')
        while TRUE:
            line = file.readline()
            line = line.split()
            if len(line) == 0:
                file.close()
                messagebox.showerror('Ошибка!', 'Неверный лигин/пароль! Если вы ещё не зарегестрированны,то пройдите регестрацию перед взодом!') 
                break
            elif line[0] == entry_username.get() and line[1] == entry_password.get():
                file.close()

                window.destroy()

                window_inf = Tk()
                window_inf.title('Информационное окно')
                window_inf.geometry('350x115')
                window_inf.resizable(False, False)

                lable_inf = Label(window_inf, text='Поздравляем! Вы успешно вошли!')
                lable_inf.pack(pady=20)

                def window_inf_destroy():
                    window_inf.destroy()

                button_start = Button(window_inf, text='Начать игру', command=lambda:[window_inf_destroy(), game()])
                button_start.pack(pady=10)

def main_account_screen():
    global window
    window = Tk()
    window.title('Авторизация')
    window.geometry('400x350')
    window.resizable(False, False)

    global username
    global password
    global entry_username
    global entry_password
    username = StringVar()
    password = StringVar()

    lable_username = Label(window, text='Введите логин:')
    lable_username.pack(pady=20)
    entry_username = Entry(window, width=50)
    entry_username.pack()

    def showpass():
        if entry_password['show'] == '*':
            entry_password['show'] = ''
        else:
            entry_password['show'] = '*'

    lable_password = Label(window, text='Введите пароль:')
    lable_password.pack(pady=20)
    entry_password = Entry(window, width=50, show='*')
    entry_password.pack()

    button_password = Button(window, text='Посмотреть пароль', command=showpass)
    button_password.pack(pady=10)

    button_entry = Button(window, text='Войти', command=check_log_in)
    button_entry.pack(pady=20)

    def window_destroy():
        window.destroy()

    button_registration = Button(window, text='Ещё не зарегестрированы? Зарегестрироваться', command=lambda:[window_destroy(), registration()])
    button_registration.pack(pady=10)

    window.mainloop()

main_account_screen()
