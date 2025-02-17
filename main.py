import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import time
import copy

def game():

    gl_okno = Tk()  # создаём окно
    gl_okno.title("Курсовая работа: Компьютерная логическая игра «Фризские шашки – Поддавки»")  # заголовок окна
    doska = Canvas(gl_okno, width=1000, height=1000, bg='#FFFFFF')
    doska.pack()

    n2_spisok = ()  # конечный список ходов компьютера
    ur = 3  # количество предсказываемых компьютером ходов
    k_rez = 0  # !!!
    o_rez = 0
    poz1_x = -1  # клетка не задана
    f_hi = True  # определение хода игрока(да)

    def izobrazheniya_peshek():  # загружаем изображения пешек
        global peshki
        i1 = PhotoImage(file="1b.gif")
        i2 = PhotoImage(file="1bk.gif")
        i3 = PhotoImage(file="1h.gif")
        i4 = PhotoImage(file="1hk.gif")
        peshki = [0, i1, i2, i3, i4]

    def novaya_igra():  # начинаем новую игру
        global pole
        pole = [[0, 3, 0, 3, 0, 3, 0, 3, 0, 3],
                [3, 0, 3, 0, 3, 0, 3, 0, 3, 0],
                [0, 3, 0, 3, 0, 3, 0, 3, 0, 3],
                [3, 0, 3, 0, 3, 0, 3, 0, 3, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]  # Создаем доску 10x10

        # Размещаем 20 шашек для каждого игрока
        # Шашки компьютера (3)
        count = 0
        for i in range(4):  # Размещаем в первых 4 рядах
            for j in range(10):
                if (i + j) % 2 != 0:  # Только на черных клетках
                    pole[i][j] = 3
                    count += 1
                    if count == 20:
                        break
            if count == 20:
                break

        # Шашки игрока (1)
        count = 0
        for i in range(9, 5, -1):  # Размещаем в последних 4 рядах
            for j in range(9, -1, -1):
                if (i + j) % 2 != 0:  # Только на черных клетках
                    pole[i][j] = 1
                    count += 1
                    if count == 20:
                        break
            if count == 20:
                break

    def vivod(x_poz_1, y_poz_1, x_poz_2, y_poz_2):  # рисуем игровое поле
        global peshki
        global pole
        global kr_ramka, zel_ramka
        k = 100  # Уменьшаем размер клетки, чтобы поместилось на экране
        x = 0
        doska.delete('all')
        kr_ramka = doska.create_rectangle(-5, -5, -5, -5, outline="red", width=5)
        zel_ramka = doska.create_rectangle(-5, -5, -5, -5, outline="green", width=5)

        while x < 10 * k:  # рисуем доску - изменили на 10
            y = 1 * k
            while y < 10 * k:  # изменили на 10
                doska.create_rectangle(x, y, x + k, y + k, fill="black")
                y += 2 * k
            x += 2 * k
        x = 1 * k
        while x < 10 * k:  # рисуем доску - изменили на 10
            y = 0
            while y < 10 * k:  # изменили на 10
                doska.create_rectangle(x, y, x + k, y + k, fill="black")
                y += 2 * k
            x += 2 * k

        for y in range(10):  # рисуем стоячие пешки - изменили на 10
            for x in range(10):  # изменили на 10
                z = pole[y][x]
                if z:
                    if (x_poz_1, y_poz_1) != (x, y):  # стоячие пешки?
                        doska.create_image(x * k, y * k, anchor=NW, image=peshki[z])
        # рисуем активную пешку
        if 0 <= y_poz_1 < 10 and 0 <= x_poz_1 < 10: # Add this check
            z = pole[y_poz_1][x_poz_1]
            if z:  # ???
                doska.create_image(x_poz_1 * k, y_poz_1 * k, anchor=NW, image=peshki[z], tag='ani')
        # вычисление коэф. для анимации
        kx = 1 if x_poz_1 < x_poz_2 else -1
        ky = 1 if y_poz_1 < y_poz_2 else -1

        # Added checks before the next loop
        if x_poz_1 != -1 and y_poz_1 != -1 and x_poz_2 != -1 and y_poz_2 != -1:
            for i in range(abs(x_poz_1 - x_poz_2)):  # анимация перемещения пешки
                for ii in range(33):
                    doska.move('ani', 0.03 * k * kx, 0.03 * k * ky)
                    doska.update()  # обновление
                    time.sleep(0.01)
    def soobsenie(s):
        global f_hi
        z = 'Игра завершена'
        if s == 1:
            i = messagebox.askyesno(title=z, message='Вы проиграли! Победил ИИ!( \nНажмите "Да" что бы начать заново.',
                                    icon='info')
        if s == 2:
            i = messagebox.askyesno(title=z, message='Вы победили!\nНажмите "Да" что бы начать заново.', icon='info')
        if s == 3:
            i = messagebox.askyesno(title=z, message='Ходов больше нет.\nНажмите "Да" что бы начать заново.', icon='info')
        if s == 4:
            i = messagebox.askyesno(title=z, message='Остались только дамки - ничья!.\nНажмите "Да" что бы начать заново.', icon='info')
        if i:
            novaya_igra()
            vivod(-1, -1, -1, -1)  # рисуем игровое поле
            f_hi = True  # ход игрока доступен

    def pozici_1(event):  # выбор клетки для хода 1
        x, y = (event.x) // 100, (event.y) // 100  # вычисляем координаты клетки
        doska.coords(zel_ramka, x * 100, y * 100, x * 100 + 100, y * 100 + 100)  # рамка в выбранной клетке

    def pozici_2(event):  # выбор клетки для хода 2
        global poz1_x, poz1_y, poz2_x, poz2_y
        global f_hi
        f_hi = True  # определение хода игрока(да)
        x, y = (event.x) // 100, (event.y) // 100  # вычисляем координаты клетки
        if pole[y][x] == 1 or pole[y][x] == 2:  # проверяем пешку игрока в выбранной клетке
            doska.coords(kr_ramka, x * 100, y * 100, x * 100 + 100, y * 100 + 100)  # рамка в выбранной клетке
            poz1_x, poz1_y = x, y
        else:
            if poz1_x != -1:  # клетка выбрана
                poz2_x, poz2_y = x, y
                if f_hi:  # ход игрока?
                    hod_igroka()
                    if not (f_hi):
                        time.sleep(0.5)
                        hod_kompjutera()  # передаём ход компьютеру
                        # gl_okno.after(500,hod_kompjutera(0))#!!!#передаём ход компьютеру
                poz1_x = -1  # клетка не выбрана
                doska.coords(kr_ramka, -5, -5, -5, -5)  # рамка вне поля

    def hod_kompjutera():  # !!!
        global f_hi
        global n2_spisok
        proverka_hk(1, (), [])
        if n2_spisok:  # проверяем наличие доступных ходов
            kh = len(n2_spisok)  # количество ходов
            th = random.randint(0, kh - 1)  # случайный ход
            dh = len(n2_spisok[th])  # длина хода
            for h in n2_spisok:  # !!!для отладки!!!
                h = h  # !!!для отладки!!!
            for i in range(dh - 1):
                # выполняем ход
                spisok = hod(1, n2_spisok[th][i][0], n2_spisok[th][i][1], n2_spisok[th][1 + i][0],
                             n2_spisok[th][1 + i][1])
            n2_spisok = []  # очищаем список ходов
            f_hi = True  # ход игрока доступен

        # определяем победителя
        s_k, s_i = skan()
        if not (s_i):
            soobsenie(2)
        elif not (s_k):
            soobsenie(1)
        elif f_hi and not (spisok_hi()):
            soobsenie(3)
        elif not (f_hi) and not (spisok_hk()):
            soobsenie(3)

    def spisok_hk():  # составляем список ходов компьютера
        spisok = prosmotr_hodov_k1([])  # здесь проверяем обязательные ходы
        if not (spisok):
            spisok = prosmotr_hodov_k2([])  # здесь проверяем оставшиеся ходы
        return spisok

    def proverka_hk(tur, n_spisok, spisok):  # !!!
        global pole
        global n2_spisok
        n2_spisok = ()  # конечный список ходов компьютера
        global l_rez, k_rez, o_rez
        if not (spisok):  # если список ходов пустой...
            spisok = spisok_hk()  # заполняем

        if spisok:
            k_pole = copy.deepcopy(pole)  # копируем поле
            for ((poz1_x, poz1_y), (poz2_x, poz2_y)) in spisok:  # проходим все ходы по списку
                t_spisok = hod(0, poz1_x, poz1_y, poz2_x, poz2_y)
                if t_spisok:  # если существует ещё ход
                    proverka_hk(tur, (n_spisok + ((poz1_x, poz1_y),)), t_spisok)
                else:
                    proverka_hi(tur, [])
                    if tur == 1:
                        t_rez = o_rez / k_rez
                        if not (n2_spisok):  # записыаем если пустой
                            n2_spisok = (n_spisok + ((poz1_x, poz1_y), (poz2_x, poz2_y)),)
                            l_rez = t_rez  # сохряняем наилучший результат
                        else:
                            if t_rez == l_rez:
                                n2_spisok = n2_spisok + (n_spisok + ((poz1_x, poz1_y), (poz2_x, poz2_y)),)
                            if t_rez > l_rez:
                                n2_spisok = ()
                                n2_spisok = (n_spisok + ((poz1_x, poz1_y), (poz2_x, poz2_y)),)
                                l_rez = t_rez  # сохряняем наилучший результат
                        o_rez = 0
                        k_rez = 0

                pole = copy.deepcopy(k_pole)  # возвращаем поле
        else:  # ???
            s_k, s_i = skan()  # подсчёт результата хода
            o_rez += (s_k - s_i)
            k_rez += 1

    def spisok_hi():  # составляем список ходов игрока
        spisok = prosmotr_hodov_i1([])  # здесь проверяем обязательные ходы
        if not (spisok):
            spisok = prosmotr_hodov_i2([])  # здесь проверяем оставшиеся ходы
        return spisok

    def proverka_hi(tur, spisok):
        global pole, k_rez, o_rez
        global ur
        k_rez = 0  # !!!
        o_rez = 0
        ur = 3  # количество предсказываемых компьютером ходов
        if not (spisok):
            spisok = spisok_hi()

        if spisok:  # проверяем наличие доступных ходов
            k_pole = copy.deepcopy(pole)  # копируем поле
            for ((poz1_x, poz1_y), (poz2_x, poz2_y)) in spisok:
                t_spisok = hod(0, poz1_x, poz1_y, poz2_x, poz2_y)
                if t_spisok:  # если существует ещё ход
                    proverka_hi(tur, t_spisok)
                else:
                    if tur < ur:
                        proverka_hk(tur + 1, (), [])
                    else:
                        s_k, s_i = skan()  # подсчёт результата хода
                        o_rez += (s_k - s_i)
                        k_rez += 1

                pole = copy.deepcopy(k_pole)  # возвращаем поле
        else:  # доступных ходов нет
            s_k, s_i = skan()  # подсчёт результата хода
            o_rez += (s_k - s_i)
            k_rez += 1

    def skan():  # подсчёт пешек на поле
        global pole
        s_i = 0
        s_k = 0
        for i in range(10):
            for ii in pole[i]:
                if ii == 1: s_i += 1
                if ii == 2: s_i += 3
                if ii == 3: s_k += 1
                if ii == 4: s_k += 3
                if ii == 5: s_k += 1
        return s_k, s_i

    def hod_igroka():
        global poz1_x, poz1_y, poz2_x, poz2_y
        global f_hi
        f_hi = False  # считаем ход игрока выполненным
        spisok = spisok_hi()
        if spisok:
            if ((poz1_x, poz1_y), (poz2_x, poz2_y)) in spisok:  # проверяем ход на соответствие правилам игры
                t_spisok = hod(1, poz1_x, poz1_y, poz2_x, poz2_y)  # если всё хорошо, делаем ход
                if t_spisok:  # если есть ещё ход той же пешкой
                    f_hi = True  # считаем ход игрока невыполненным
            else:
                f_hi = True  # считаем ход игрока невыполненным
        doska.update()  # !!!обновление

    def hod(f, poz1_x, poz1_y, poz2_x, poz2_y):
        global pole
        if f: vivod(poz1_x, poz1_y, poz2_x, poz2_y)  # рисуем игровое поле

        # превращение
        if poz2_y == 0 and pole[poz1_y][poz1_x] == 1:
            pole[poz1_y][poz1_x] = 2  # Player piece becomes king
        if poz2_y == 9 and pole[poz1_y][poz1_x] == 3:
            pole[poz1_y][poz1_x] = 4  # AI piece becomes king

        # делаем ход
        pole[poz2_y][poz2_x] = pole[poz1_y][poz1_x]
        pole[poz1_y][poz1_x] = 0

        # рубим пешку игрока
        kx = ky = 1
        if poz1_x < poz2_x: kx = -1
        if poz1_y < poz2_y: ky = -1
        x_poz, y_poz = poz2_x, poz2_y
        while (poz1_x != x_poz) or (poz1_y != y_poz):
            x_poz += kx
            y_poz += ky
            if pole[y_poz][x_poz] != 0 and (x_poz, y_poz) != (poz1_x, poz1_y): # Ensure not removing the origin
                pole[y_poz][x_poz] = 0
                if f: vivod(-1, -1, -1, -1)  # рисуем игровое поле

                # проверяем ход той же пешкой...
                if pole[poz2_y][poz2_x] == 3 or pole[poz2_y][poz2_x] == 4:  # ...компьютера
                    return prosmotr_hodov_k1p([], poz2_x, poz2_y)  # возвращаем список доступных ходов
                elif pole[poz2_y][poz2_x] == 1 or pole[poz2_y][poz2_x] == 2:  # ...игрока
                    return prosmotr_hodov_i1p([], poz2_x, poz2_y)  # возвращаем список доступных ходов

        if f: vivod(poz1_x, poz1_y, poz2_x, poz2_y)  # рисуем игровое поле

    def prosmotr_hodov_k1(spisok):  # проверка наличия обязательных ходов
        for y in range(10):  # сканируем всё поле
            for x in range(10):
                spisok = prosmotr_hodov_k1p(spisok, x, y)
        return spisok

    def prosmotr_hodov_k1p(spisok, x, y):
        if pole[y][x] == 3:  # пешка
            for ix, iy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if 0 <= y + iy * 2 <= 9 and 0 <= x + ix * 2 <= 9:
                    if pole[y + iy][x + ix] == 1 or pole[y + iy][x + ix] == 2:
                        if pole[y + iy * 2][x + ix * 2] == 0:
                            spisok.append(((x, y), (x + ix * 2, y + iy * 2)))  # запись хода в конец списка
        elif pole[y][x] == 4:  # пешка с короной
            for ix, iy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                osh = 0  # определение правильности хода
                for i in range(1, 10):
                    new_y = y + iy * i
                    new_x = x + ix * i
                    if 0 <= new_y <= 9 and 0 <= new_x <= 9:
                        if pole[new_y][new_x] == 0 and osh == 0:
                            spisok.append(((x, y), (new_x, new_y)))  # запись хода в конец списка
                        elif (pole[new_y][new_x] == 1 or pole[new_y][new_x] == 2) and osh == 0:
                            osh = 1
                        elif osh == 1:
                            new_y_jump = y + iy * (i + 1)
                            new_x_jump = x + ix * (i + 1)
                            if 0 <= new_y_jump <= 9 and 0 <= new_x_jump <= 9:
                               if pole[new_y_jump][new_x_jump] == 0: # can jump
                                   spisok.append(((x, y), (new_x_jump, new_y_jump)))
                                   osh = 2
                            else:
                                break
                        else:
                            break
                    else:
                        break
            if pole[y][x] == 4 and pole[y][x] == 2:
                soobsenie(4)
        return spisok

    def prosmotr_hodov_k2(spisok):  # проверка наличия остальных ходов
        for y in range(10):  # сканируем всё поле
            for x in range(10):
                if pole[y][x] == 3:  # пешка
                    # Prioritize moves that put the checker next to an enemy
                    for ix, iy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:  # All adjacent squares
                        if 0 <= y + iy <= 9 and 0 <= x + ix <= 9:
                            if pole[y + iy][x + ix] == 0:  # Empty
                                # Check if any enemy is nearby this square
                                enemy_nearby = False
                                for ex, ey in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                                    if 0 <= y + iy + ey <= 9 and 0 <= x + ix + ex <= 9:  # check nearby cells
                                        if pole[y + iy + ey][x + ix + ex] in (1, 2):
                                            enemy_nearby = True
                                            break
                                if enemy_nearby:
                                    spisok.append(((x, y), (x + ix, y + iy)))  # Move closer to the enemy!
                    # Normal moves that still can be made if no enemy is close
                    for ix, iy in [(-1, 1), (1, 1)]:  # Normal moves for AI (forward)
                        if 0 <= y + iy <= 9 and 0 <= x + ix <= 9:
                            if pole[y + iy][x + ix] == 0:
                                spisok.append(((x, y), (x + ix, y + iy)))  # Offer the checker
                elif pole[y][x] == 4:  # дамка (Queen)
                    # Prioritize moves that put the checker next to an enemy
                    for ix, iy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        for i in range(1, 10):  # короны can move further
                            if 0 <= y + iy * i <= 9 and 0 <= x + ix * i <= 9:
                                enemy_nearby = False  # check and see if enemy is nearby
                                for ex, ey in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                                    if 0 <= y + iy * i + ey <= 9 and 0 <= x + ix * i + ex <= 9:  # check nearby cells
                                        if pole[y + iy * i + ey][x + ix * i + ex] in (1, 2):
                                            enemy_nearby = True
                                            break
                                if enemy_nearby:
                                    spisok.append(((x, y), (x + ix * i, y + iy * i)))

                    # If no closer moves can be found, still offer
                    for ix, iy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        for i in range(1, 10):  # короны can move further
                            if 0 <= y + iy * i <= 9 and 0 <= x + ix * i <= 9:
                                if pole[y + iy * i][x + ix * i] == 0:
                                    spisok.append(((x, y), (x + ix * i, y + iy * i)))  # Offer the checker

        return spisok

    def prosmotr_hodov_i1(spisok):  # проверка наличия обязательных ходов
        spisok = []  # список ходов
        for y in range(10):  # сканируем всё поле
            for x in range(10):
                spisok = prosmotr_hodov_i1p(spisok, x, y)
        return spisok

    def prosmotr_hodov_i1p(spisok, x, y):
        if pole[y][x] == 1:  # пешка
            for ix, iy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if 0 <= y + iy + iy <= 9 and 0 <= x + ix + ix <= 9:
                    if pole[y + iy][x + ix] == 3 or pole[y + iy][x + ix] == 4:
                        if pole[y + iy + iy][x + ix + ix] == 0:
                            spisok.append(((x, y), (x + ix + ix, y + iy + iy)))  # запись хода в конец списка
        elif pole[y][x] == 2:  # пешка с короной
            for ix, iy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                osh = 0  # определение правильности хода
                for i in range(1, 10):
                    if 0 <= y + iy * i <= 9 and 0 <= x + ix * i <= 9:
                        if pole[y + iy * i][x + ix * i] == 0 and osh == 0:
                            spisok.append(((x, y), (x + ix * i, y + iy * i)))  # запись хода в конец списка
                        elif (pole[y + iy * i][x + ix * i] == 3 or pole[y + iy * i][x + ix * i] == 4) and osh == 0:
                            osh = 1
                        elif (pole[y + iy * i][x + ix * i] == 1 or pole[y + iy * i][x + ix * i] == 2 or osh > 1):
                            break
                        elif osh == 1 and (0 <= y + iy * (i + 1) <= 9) and (0 <= x + ix * (i + 1) <= 9) and pole[y + iy * (i + 1)][x + ix * (i + 1)] == 0: # can jump
                            spisok.append(((x, y), (x + ix * (i + 1), y + iy * (i + 1))))
                            osh = 2

        return spisok

    def prosmotr_hodov_i2(spisok):  # проверка наличия остальных ходов
        for y in range(10):  # сканируем всё поле
            for x in range(10):
                if pole[y][x] == 1:  # пешка
                    for ix, iy in [(-1, -1), (1, -1)]:
                        if 0 <= y + iy <= 9 and 0 <= x + ix <= 9:
                            if pole[y + iy][x + ix] == 0:
                                spisok.append(((x, y), (x + ix, y + iy)))  # запись хода в конец списка
                elif pole[y][x] == 2:  # пешка с короной
                    for ix, iy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        osh = 0  # определение правильности хода
                        for i in range(1, 10):
                            if 0 <= y + iy * i <= 9 and 0 <= x + ix * i <= 9:
                                if pole[y + iy * i][x + ix * i] == 0 and osh == 0:
                                    spisok.append(((x, y), (x + ix * i, y + iy * i)))  # запись хода в конец списка
                                elif (pole[y + iy * i][x + ix * i] == 3 or pole[y + iy * i][x + ix * i] == 4) and osh == 0:
                                    osh = 1
                                elif (pole[y + iy * i][x + ix * i] == 1 or pole[y + iy * i][x + ix * i] == 2 or osh >= 1):
                                    break
                                elif osh == 1 and (0 <= y + iy * (i+1) <= 9) and (0 <= x + ix * (i+1) <= 9) and pole[y + iy * (i+1)][x + ix * (i+1)] == 0: # can jump
                                    spisok.append(((x, y), (x + ix * (i + 1), y + iy * (i + 1))))
                                    osh = 2
                if pole[y][x] == 4 and pole[y][x] == 2:
                    soobsenie(4)
        return spisok

    izobrazheniya_peshek()  # здесь загружаем изображения пешек
    novaya_igra()  # начинаем новую игру
    vivod(-1, -1, -1, -1)  # рисуем игровое поле
    doska.bind("<Motion>", pozici_1)  # движение мышки по полю
    doska.bind("<Button-1>", pozici_2)  # нажатие левой кнопки

    mainloop()

def check_registration():
    global file
    check_login = entry_username_r.get()
    check_password = entry_password_r.get()
    if (check_login == '') or (check_password == '') or ((check_login == '') and (check_password == '')):
        messagebox.showerror('Информационное окно', 'Ошибка! Заполните пустое поле / пустые поля!')
    if len(check_login) < 6 or len(check_password) < 6:
        messagebox.showerror("Ошибка регистрации!", "Логин и пароль должны состоять не менее чем из 6 символов!")
    else:
        file = open('login.txt', 'w')
        file.write(entry_username_r.get() + ' ' + entry_password_r.get() + '\n')
        #file.close()

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
        line = file.readline().split()
        for j in range(len(line)):  # ищем совпадение логин и пароль
            if line[j] != check_login_1 and line[j + 1] != check_password_1:
                messagebox.showerror('Ошибка!', 'Неверный лигин/пароль!')
                break
            elif line[j] == check_login_1 and line[j +1] == check_password_1:
                #file.close()

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
                break

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
