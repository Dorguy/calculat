import math
import tkinter as tk
from tkinter import messagebox

import numpy as np

import starting


# Ограничение ввода символов
def validate_e(new_value):
    try:
        if new_value == "" or new_value == "-":
            return True
        _str = str(float(new_value))
        return True
    except:
        return False


#
def add_magic(entry):
    x = y = s = ''
    for i in range(len(entry)):
        if entry[i] in ['+', '-', '×', '÷']:
            x = y
            y = ''
            s = entry[i]
        else:
            y += entry[i]
    return x, y, s


# Стереть всё
def Delete_0(Del):
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, '0')
    calc_etry['state'] = tk.DISABLED


# Стереть последний элемент
def Delete_1(Del):
    entry = calc_etry.get()
    entry = entry[:-1]
    if len(entry) == 0:
        entry = '0'
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED


# Стереть всё после символа операции
def Delete_2(Del):
    entry = calc_etry.get()
    entry_0, entry_1, sim = add_magic(entry)
    if sim == '':
        entry = '0'
    else:
        entry = entry_0 + sim
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED


# Противоположный элемент
def neg(neg):
    entry = calc_etry.get()
    global HZ
    HZ = 2
    if ('+' in entry) or ('-' in entry) or ('×' in entry) or ('÷' in entry):
        if entry[-1] in ['+', '-', '×', '÷']:
            entry = entry + entry[:-1]
        entry = add_calculation_0(entry)
    entry = float(entry) * (-1)
    if entry == int(entry):
        entry = str(int(entry))
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED


# Сложение
def add_pl(x, y):
    if type(x) == float and type(y) == float:
        return str(x + y)
    else:
        raise TypeError


# Вычитание
def add_mi(x, y):
    if type(x) == float and type(y) == float:
        return str(x - y)
    else:
        raise TypeError


# Умножение
def add_um(x, y):
    if type(x) == float and type(y) == float:
        return str(x * y)
    else:
        raise TypeError


# Деление
def add_de(x, y):
    if type(x) == float and type(y) == float:
        try:
            return str(x / y)
        except ZeroDivisionError:

            messagebox.showerror('Ошибка', 'Деление на ноль невозможно')
            return 0
    else:
        raise TypeError


# Знаменатель "⅟х"
def denominator(denominator):
    entry = calc_etry.get()
    global HZ
    HZ = 1
    if ('+' in entry) or ('-' in entry) or ('×' in entry) or ('÷' in entry):
        if entry[-1] in ['+', '-', '×', '÷']:
            entry = entry + entry[:-1]
        entry = add_calculation_0(entry)
    try:
        entry = 1 / float(entry)
        if entry == int(entry):
            entry = str(int(entry))
        calc_etry['state'] = tk.NORMAL
        calc_etry.delete(0, tk.END)
        calc_etry.insert(0, entry)
        calc_etry['state'] = tk.DISABLED
    except ZeroDivisionError:
        messagebox.showerror('Ошибка', 'Деление на ноль невозможно')
        calc_etry['state'] = tk.NORMAL
        calc_etry.delete(0, tk.END)
        calc_etry.insert(0, '0')
        calc_etry['state'] = tk.DISABLED


# Квадрат "x²"
def sq(square):
    entry = calc_etry.get()
    global HZ
    HZ = 1
    if ('+' in entry) or ('-' in entry) or ('×' in entry) or ('÷' in entry):
        if entry[-1] in ['+', '-', '×', '÷']:
            entry = entry + entry[:-1]
        entry = add_calculation_0(entry)
    entry = float(entry) ** 2
    if entry == int(entry):
        entry = str(int(entry))
    t = entry
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED
    return t


# Квадратный корень "√х"
def sq_r(square_root):
    entry = calc_etry.get()
    global HZ
    HZ = 1
    if ('+' in entry) or ('-' in entry) or ('×' in entry) or ('÷' in entry):
        if entry[-1] in ['+', '-', '×', '÷']:
            entry = entry + entry[:-1]
        entry = add_calculation_0(entry)
    entry = float(entry) ** 0.5
    if entry == int(entry):
        entry = str(int(entry))
    t = entry
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED
    return t


# Pасчёт_1
def add_calculation_1(S, x, y):
    try:
        if S == '+':
            calculation = add_pl(x, y)
        elif S == '-':
            calculation = add_mi(x, y)
        elif S == '×':
            calculation = add_um(x, y)
        elif S == '÷':
            calculation = add_de(x, y)
        return calculation
    except:
        raise TypeError


# Pасчёт_0; Разбиваем строку на 2 числа и символ между ними
def add_calculation_0(entry):
    try:
        x, y = 0, ''
        S = mod_x = ''
        a = []
        if entry[0] == '-':
            mod_x = '-'
            entry = entry[1:]
        while entry != '':
            i = len(entry) - 1
            a.append(entry[i])
            entry = entry[:i]
        a.reverse()
        for i in a:
            if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                y += i
            else:
                S = i
                x = y
                y = ''
        x = float(x)
        if mod_x != '':
            x *= (-1)
        y = float(y)
        if S != '':
            entry = float(add_calculation_1(S, x, y))
        else:
            entry = float(calc_etry.get())
        if entry == int(entry):
            entry = int(entry)
        return str(entry)
    except:
        raise TypeError


# Добавить цифру
def add_digit(digit):
    entry = calc_etry.get()
    global HZ
    if HZ == 1:
        entry = '0'
        HZ = 0
    if entry[0] == '0' and len(entry) == 1:
        entry = entry[1:]
    if (len(entry) > 1) and (entry[-1] == '0') and (entry[-2] in ['+', '-', '×', '÷']) and (digit != '.'):
        entry = entry[:-1]
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry + digit)
    calc_etry['state'] = tk.DISABLED


# Добавить знак
def add_sign(sing):
    global HZ
    HZ = 0
    entry_0 = calc_etry.get()
    if sing in ['.']:
        K = 0
        for i in range(len(entry_0)):
            if entry_0[i] in ['+', '-', '×', '÷'] and (i != len(entry_0) - 1):
                K = 0
            elif entry_0[i] in ['.']:
                K += 1
        if K > 0:
            sing = ''
    if entry_0[-1] in ['+', '-', '×', '÷', '.'] and sing != '':
        entry = entry_0[:-1] + sing
    else:
        entry = entry_0 + sing
    if entry[-1] in ['+', '-', '×', '÷'] and (
            '+' in entry[:-1] or '-' in entry[:-1] or '×' in entry[:-1] or '÷' in entry[:-1]):
        entry = str(add_calculation_0(entry[:-1])) + entry[-1]
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED


# Равно
def equally(eq):
    global HZ
    HZ = 1
    entry = calc_etry.get()
    if entry[-1] in ['+', '-', '×', '÷']:
        entry = entry + entry[:-1]
    entry = str(add_calculation_0(entry))
    calc_etry['state'] = tk.NORMAL
    calc_etry.delete(0, tk.END)
    calc_etry.insert(0, entry)
    calc_etry['state'] = tk.DISABLED


# Меню
def menu(calc):
    menu_top = tk.Toplevel(calc)
    # menu_top.overrideredirect(True)
    menu_top['bg'] = '#09bd87'
    menu_top.minsize(width=380, height=500)
    menu_top.maxsize(width=380, height=500)
    tk.Button(menu_top, text='Игра', bd=3, bg='#f0ffff', font=('Arial', 13), command=lambda: game()).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  sticky='wens',
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    tk.Button(menu_top, text='Вычисление опеределителя целых чисел', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: okno_opredelit(menu_top)).grid(row=1, column=0, sticky='wens', padx=2, pady=2)
    tk.Button(menu_top, text='Квадратное уравнение', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: okno_kv_ur(menu_top)).grid(row=2, column=0, sticky='wens', padx=2, pady=2)
    tk.Button(menu_top, text='Угол между векторами', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: ugol_vector(menu_top)).grid(row=3, column=0, sticky='wens', padx=2, pady=2)


# нахождение угла между векторами
def ugol_vector(t):
    ugol = tk.Toplevel(t)
    ugol.minsize(width=400, height=200)
    ugol['bg'] = '#09bd87'
    ugol.grid()
    ugol.title('Угол между векторами')
    bcmd = (ugol.register(validate_e), '%P')
    b0 = tk.Entry(ugol, font=('Times', 15), width=50, justify=tk.CENTER, bd=3)
    b0.insert(0, 'Введите координаты')
    b0['state'] = tk.DISABLED
    b0.config(background='#000000', disabledbackground='#f8ffff')
    b0.grid(row=0, column=0, sticky='we', columnspan=4)
    b1 = tk.Entry(ugol, font=('Times', 15), width=30, justify=tk.LEFT, bd=3)
    b1.insert(0, 'Координаты 1ого вектора:')
    b1['state'] = tk.DISABLED
    b1.config(background='#000000', disabledbackground='#f8ffff')
    b1.grid(row=1, column=0, sticky='wens', pady=3)
    b2 = tk.Entry(ugol, font=('Times', 15), width=2, justify=tk.CENTER, bd=5, bg='#f8ffff', validate='key',
                  validatecommand=bcmd)
    # b2['state'] = tk.DISABLED
    b2.grid(row=1, column=1, padx=3, pady=3, sticky='wens')
    b2.focus()
    b3 = tk.Entry(ugol, font=('Times', 15), width=2, justify=tk.CENTER, bd=5, bg='#f8ffff', validate='key',
                  validatecommand=bcmd)
    # b3['state'] = tk.DISABLED
    b3.grid(row=1, column=2, padx=3, pady=3, sticky='wens')
    b3.focus()
    b4 = tk.Entry(ugol, font=('Times', 15), width=2, justify=tk.CENTER, bd=5, bg='#f8ffff', validate='key',
                  validatecommand=bcmd)
    # b4['state'] = DISABLED
    b4.grid(row=1, column=3, padx=3, pady=3, sticky='wens')
    b4.focus()
    b5 = tk.Entry(ugol, font=('Times', 15), width=30, justify=tk.LEFT, bd=3)
    b5.insert(0, 'Координаты 2ого вектора:')
    b5['state'] = tk.DISABLED
    b5.config(background='#000000', disabledbackground='#f8ffff')
    b5.grid(row=2, column=0, sticky='wens', pady=3)
    b6 = tk.Entry(ugol, font=('Times', 15), width=2, justify=tk.CENTER, bd=5, bg='#f8ffff', validate='key',
                  validatecommand=bcmd)
    # b6['state'] = tk.DISABLED
    b6.grid(row=2, column=1, padx=3, pady=3, sticky='wens')
    b6.focus()
    b7 = tk.Entry(ugol, font=('Times', 15), width=2, justify=tk.CENTER, bd=5, bg='#f8ffff', validate='key',
                  validatecommand=bcmd)
    # b7['state'] = DISABLED
    b7.grid(row=2, column=2, padx=3, pady=3, sticky='wens')
    b7.focus()
    b8 = tk.Entry(ugol, font=('Times', 15), width=2, justify=tk.CENTER, bd=5, bg='#f8ffff', validate='key',
                  validatecommand=bcmd)
    # b8['state'] = DISABLED
    b8.grid(row=2, column=3, padx=3, pady=3, sticky='wens')
    b8.focus()
    tk.Button(ugol, text='OK', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: Ugol2(b2, b3, b4, b6, b7, b8, ugol)).grid(row=3, column=0, sticky='wens', padx=2, pady=2,
                                                                        columnspan=1)


# подсчет и вывод угла в градусах
def Ugol2(b2, b3, b4, b6, b7, b8, ugol):
    a1 = b2.get()
    if a1 == '':
        a1 = '0'
        b2.insert(0, '0')
    a1 = int(a1)
    b1 = b3.get()
    if b1 == '':
        b1 = '0'
        b3.insert(0, '0')
    b1 = int(b1)
    c1 = b4.get()
    if c1 == '':
        c1 = '0'
        b4.insert(0, '0')
    c1 = int(c1)
    a2 = b6.get()
    if a2 == '':
        a2 = '0'
        b6.insert(0, '0')
    a2 = int(a2)
    d2 = b7.get()
    if d2 == '':
        d2 = '0'
        b7.insert(0, '0')
    d2 = int(d2)
    c2 = b8.get()
    if c2 == '':
        c2 = '0'
        b8.insert(0, '0')
    c2 = int(c2)
    p = math.pi
    a = np.array([[a1, b1, c1]])
    b = np.array([[a2, d2, c2]])
    b_transp = b.T
    ugolR = (np.arccos((np.matmul(a, b_transp)) / (np.linalg.norm(a) * np.linalg.norm(b))))
    ugolG = (ugolR) * 180 / p
    t = np.round(ugolG, 2)
    q = str(t)
    q = q.replace('[', '')
    q = q.replace(']', '')
    q = q.replace('.', '°')
    e_x = tk.Entry(ugol, font=('Times', 15), width=3, justify=tk.LEFT, bd=0, highlightthickness=0)
    e_x.insert(0, '⍺      = ')
    e_x['state'] = tk.DISABLED
    e_x.config(background='#000000', disabledbackground='#f8ffff')
    e_x.grid(row=4, column=1, columnspan=1, pady=3, sticky='wens')
    e_xx = tk.Entry(ugol, font=('Times', 15), width=6, justify=tk.CENTER, bd=0, highlightthickness=0)
    e_xx['state'] = tk.DISABLED
    e_xx.config(background='#000000', disabledbackground='#f8ffff')
    e_xx.grid(row=4, column=2, columnspan=1, pady=3, sticky='wens')
    e_xx['state'] = tk.NORMAL
    e_xx.delete(0, tk.END)
    e_xx.insert(0, q)
    e_xx['state'] = tk.DISABLED


# окно для выбора размера определителя
def okno_opredelit(t):
    matr1 = tk.Toplevel(t)
    matr1.minsize(width=320, height=500)
    matr1['bg'] = '#09bd87'
    matr1.grid()
    matr1.title('Вычисление определителя')
    tk.Button(matr1, text='2*2', bd=3, bg='#f0ffff', font=('Arial', 13), command=lambda: opred2(matr1)).grid(row=0,
                                                                                                             column=0,
                                                                                                             sticky='wens',
                                                                                                             padx=2,
                                                                                                             pady=2)
    tk.Button(matr1, text='3*3', bd=3, bg='#f0ffff', font=('Arial', 13), command=lambda: opred3(matr1)).grid(row=1,
                                                                                                             column=0,
                                                                                                             sticky='wens',
                                                                                                             padx=2,
                                                                                                             pady=2)
    tk.Button(matr1, text='4*4', bd=3, bg='#f0ffff', font=('Arial', 13), command=lambda: opred4(matr1)).grid(row=2,
                                                                                                             column=0,
                                                                                                             sticky='wens',
                                                                                                             padx=2,
                                                                                                             pady=2)
    tk.Button(matr1, text='5*5', bd=3, bg='#f0ffff', font=('Arial', 13), command=lambda: opred5(matr1)).grid(row=3,
                                                                                                             column=0,
                                                                                                             sticky='wens',
                                                                                                             padx=2,
                                                                                                             pady=2)


def game():
    flag = True
    starting.go()
    return flag


# ввод определителя 2*2
def opred2(t):
    opred_2 = tk.Toplevel(t)
    opred_2.minsize(width=320, height=320)
    opred_2['bg'] = '#09bd87'
    opred_2.grid()
    opred_2.title('Определитель 2*2')
    b1 = tk.Entry(opred_2, font=('Times', 15), width=2, justify=tk.CENTER)
    b1.insert(0, '0')
    # b1['state'] = DISABLED
    b1.grid(row=0, column=0, padx=3, pady=3)
    b2 = tk.Entry(opred_2, font=('Times', 15), width=2, justify=tk.CENTER)
    b2.insert(0, '0')
    # b2['state'] = tk.DISABLED
    b2.grid(row=0, column=1, padx=3, pady=3)
    b3 = tk.Entry(opred_2, font=('Times', 15), width=2, justify=tk.CENTER)
    b3.insert(0, '0')
    # b3['state'] = tk.DISABLED
    b3.grid(row=1, column=0, padx=3, pady=3)
    b4 = tk.Entry(opred_2, font=('Times', 15), width=2, justify=tk.CENTER)
    b4.insert(0, '0')
    # b4['state'] = DISABLED
    b4.grid(row=1, column=1, padx=3, pady=3)
    tk.Button(opred_2, text='OK', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: mas_2(b1, b2, b3, b4, opred_2)).grid(row=2, column=c, sticky='wens', padx=2, pady=2)


# подсчет определителя 2*2
def mas_2(b1, b2, b3, b4, opred_2):
    a1 = int(b1.get())
    a2 = int(b2.get())
    a3 = int(b3.get())
    a4 = int(b4.get())
    A = np.matrix([[a1, a2], [a3, a4]])
    V = int(np.linalg.det(A))
    e_x = tk.Entry(opred_2, font=('Times', 15), width=10, justify=tk.LEFT, bd=0, highlightthickness=0)
    e_x.insert(0, 'V  = ')
    e_x['state'] = tk.DISABLED
    e_x.grid(row=5, column=1, columnspan=5, pady=3)
    e_xx = tk.Entry(opred_2, font=('Times', 15), width=6, justify=tk.CENTER, bd=0, highlightthickness=0)
    e_xx['state'] = tk.DISABLED
    e_xx.grid(row=5, column=2, columnspan=6, pady=3)
    e_xx['state'] = tk.NORMAL
    e_xx.delete(0, tk.END)
    e_xx.insert(0, V)
    e_xx['state'] = tk.DISABLED


# ввод определителя 3*3
def opred3(t):
    opred_3 = tk.Toplevel(t)
    opred_3.minsize(width=320, height=320)
    opred_3['bg'] = '#09bd87'
    opred_3.grid()
    opred_3.title('Определитель 2*2')
    b1 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b1.insert(0, '0')
    # b1['state'] = DISABLED
    b1.grid(row=0, column=0, padx=3, pady=3)
    b2 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b2.insert(0, '0')
    # b2['state'] = tk.DISABLED
    b2.grid(row=0, column=1, padx=3, pady=3)
    b3 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b3.insert(0, '0')
    # b3['state'] = tk.DISABLED
    b3.grid(row=0, column=2, padx=3, pady=3)
    b4 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b4.insert(0, '0')
    # b4['state'] = DISABLED
    b4.grid(row=1, column=0, padx=3, pady=3)
    b5 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b5.insert(0, '0')
    # b5['state'] = DISABLED
    b5.grid(row=1, column=1, padx=3, pady=3)
    b6 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b6.insert(0, '0')
    # b6['state'] = tk.DISABLED
    b6.grid(row=1, column=2, padx=3, pady=3)
    b7 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b7.insert(0, '0')
    # b7['state'] = tk.DISABLED
    b7.grid(row=2, column=0, padx=3, pady=3)
    b8 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b8.insert(0, '0')
    # b8['state'] = DISABLED
    b8.grid(row=2, column=1, padx=3, pady=3)
    b9 = tk.Entry(opred_3, font=('Times', 15), width=2, justify=tk.CENTER)
    b9.insert(0, '0')
    # b9['state'] = DISABLED
    b9.grid(row=2, column=2, padx=3, pady=3)
    tk.Button(opred_3, text='OK', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: mas_3(b1, b2, b3, b4, b5, b6, b7, b8, b9, opred_3)).grid(row=3, column=c, sticky='wens',
                                                                                       padx=2, pady=2)


# подсчет определителя 3*3
def mas_3(b1, b2, b3, b4, b5, b6, b7, b8, b9, opred_3):
    a1 = int(b1.get())
    a2 = int(b2.get())
    a3 = int(b3.get())
    a4 = int(b4.get())
    a5 = int(b5.get())
    a6 = int(b6.get())
    a7 = int(b7.get())
    a8 = int(b8.get())
    a9 = int(b9.get())
    A = np.matrix([[a1, a2, a3], [a4, a5, a6], [a7, a8, a9]])
    V = int(np.linalg.det(A))
    e_x = tk.Entry(opred_3, font=('Times', 15), width=10, justify=tk.LEFT, bd=0, highlightthickness=0)
    e_x.insert(0, 'V  = ')
    e_x['state'] = tk.DISABLED
    e_x.grid(row=5, column=1, columnspan=5, pady=3)
    e_xx = tk.Entry(opred_3, font=('Times', 15), width=6, justify=tk.CENTER, bd=0, highlightthickness=0)
    e_xx['state'] = tk.DISABLED
    e_xx.grid(row=5, column=2, columnspan=6, pady=3)
    e_xx['state'] = tk.NORMAL
    e_xx.delete(0, tk.END)
    e_xx.insert(0, V)
    e_xx['state'] = tk.DISABLED


# ввод определителя 4*4
def opred4(t):
    opred_4 = tk.Toplevel(t)
    opred_4.minsize(width=320, height=320)
    opred_4['bg'] = '#09bd87'
    opred_4.grid()
    opred_4.title('Определитель 2*2')
    b1 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b1.insert(0, '0')
    # b1['state'] = DISABLED
    b1.grid(row=0, column=0, padx=3, pady=3)
    b2 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b2.insert(0, '0')
    # b2['state'] = tk.DISABLED
    b2.grid(row=0, column=1, padx=3, pady=3)
    b3 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b3.insert(0, '0')
    # b3['state'] = tk.DISABLED
    b3.grid(row=0, column=2, padx=3, pady=3)
    b4 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b4.insert(0, '0')
    # b4['state'] = DISABLED
    b4.grid(row=0, column=3, padx=3, pady=3)
    b5 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b5.insert(0, '0')
    # b5['state'] = DISABLED
    b5.grid(row=1, column=0, padx=3, pady=3)
    b6 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b6.insert(0, '0')
    # b6['state'] = tk.DISABLED
    b6.grid(row=1, column=1, padx=3, pady=3)
    b7 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b7.insert(0, '0')
    # b7['state'] = tk.DISABLED
    b7.grid(row=1, column=2, padx=3, pady=3)
    b8 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b8.insert(0, '0')
    # b8['state'] = DISABLED
    b8.grid(row=1, column=3, padx=3, pady=3)
    b9 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b9.insert(0, '0')
    # b9['state'] = DISABLED
    b9.grid(row=2, column=0, padx=3, pady=3)
    b10 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b10.insert(0, '0')
    # b10['state'] = DISABLED
    b10.grid(row=2, column=1, padx=3, pady=3)
    b11 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b11.insert(0, '0')
    # b11['state'] = DISABLED
    b11.grid(row=2, column=2, padx=3, pady=3)
    b12 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b12.insert(0, '0')
    # b12['state'] = DISABLED
    b12.grid(row=2, column=3, padx=3, pady=3)
    b13 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b13.insert(0, '0')
    # b13['state'] = DISABLED
    b13.grid(row=3, column=0, padx=3, pady=3)
    b14 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b14.insert(0, '0')
    # b14['state'] = DISABLED
    b14.grid(row=3, column=1, padx=3, pady=3)
    b15 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b15.insert(0, '0')
    # b15['state'] = DISABLED
    b15.grid(row=3, column=2, padx=3, pady=3)
    b16 = tk.Entry(opred_4, font=('Times', 15), width=2, justify=tk.CENTER)
    b16.insert(0, '0')
    # b16['state'] = DISABLED
    b16.grid(row=3, column=3, padx=3, pady=3)
    tk.Button(opred_4, text='OK', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: mas_4(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16,
                                    opred_4)).grid(row=4, column=c, sticky='wens', padx=2, pady=2)


# подсчет определителя 4*4
def mas_4(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, opred_4):
    a1 = int(b1.get())
    a2 = int(b2.get())
    a3 = int(b3.get())
    a4 = int(b4.get())
    a5 = int(b5.get())
    a6 = int(b6.get())
    a7 = int(b7.get())
    a8 = int(b8.get())
    a9 = int(b9.get())
    a10 = int(b10.get())
    a11 = int(b11.get())
    a12 = int(b12.get())
    a13 = int(b13.get())
    a14 = int(b14.get())
    a15 = int(b15.get())
    a16 = int(b16.get())
    A = np.matrix([[a1, a2, a3, a4], [a5, a6, a7, a8], [a9, a10, a11, a12], [a13, a14, a15, a16]])
    V = int(np.linalg.det(A))
    e_x = tk.Entry(opred_4, font=('Times', 15), width=10, justify=tk.LEFT, bd=0, highlightthickness=0)
    e_x.insert(0, 'V  = ')
    e_x['state'] = tk.DISABLED
    e_x.grid(row=5, column=1, columnspan=5, pady=3)
    e_xx = tk.Entry(opred_4, font=('Times', 15), width=6, justify=tk.CENTER, bd=0, highlightthickness=0)
    e_xx['state'] = tk.DISABLED
    e_xx.grid(row=5, column=2, columnspan=6, pady=3)
    e_xx['state'] = tk.NORMAL
    e_xx.delete(0, tk.END)
    e_xx.insert(0, V)
    e_xx['state'] = tk.DISABLED


# ввод определителя 5*5
def opred5(t):
    opred_5 = tk.Toplevel(t)
    opred_5.minsize(width=320, height=320)
    opred_5['bg'] = '#09bd87'
    opred_5.grid()
    opred_5.title('Определитель 2*2')
    b1 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b1.insert(0, '0')
    # b1['state'] = DISABLED
    b1.grid(row=0, column=0, padx=3, pady=3)
    b2 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b2.insert(0, '0')
    # b2['state'] = tk.DISABLED
    b2.grid(row=0, column=1, padx=3, pady=3)
    b3 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b3.insert(0, '0')
    # b3['state'] = tk.DISABLED
    b3.grid(row=0, column=2, padx=3, pady=3)
    b4 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b4.insert(0, '0')
    # b4['state'] = DISABLED
    b4.grid(row=0, column=3, padx=3, pady=3)
    b5 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b5.insert(0, '0')
    # b5['state'] = DISABLED
    b5.grid(row=0, column=4, padx=3, pady=3)
    b6 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b6.insert(0, '0')
    # b6['state'] = tk.DISABLED
    b6.grid(row=1, column=0, padx=3, pady=3)
    b7 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b7.insert(0, '0')
    # b7['state'] = tk.DISABLED
    b7.grid(row=1, column=1, padx=3, pady=3)
    b8 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b8.insert(0, '0')
    # b8['state'] = DISABLED
    b8.grid(row=1, column=2, padx=3, pady=3)
    b9 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b9.insert(0, '0')
    # b9['state'] = DISABLED
    b9.grid(row=1, column=3, padx=3, pady=3)
    b10 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b10.insert(0, '0')
    # b10['state'] = DISABLED
    b10.grid(row=1, column=4, padx=3, pady=3)
    b11 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b11.insert(0, '0')
    # b11['state'] = DISABLED
    b11.grid(row=2, column=0, padx=3, pady=3)
    b12 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b12.insert(0, '0')
    # b12['state'] = DISABLED
    b12.grid(row=2, column=1, padx=3, pady=3)
    b13 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b13.insert(0, '0')
    # b13['state'] = DISABLED
    b13.grid(row=2, column=2, padx=3, pady=3)
    b14 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b14.insert(0, '0')
    # b14['state'] = DISABLED
    b14.grid(row=2, column=3, padx=3, pady=3)
    b15 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b15.insert(0, '0')
    # b15['state'] = DISABLED
    b15.grid(row=2, column=4, padx=3, pady=3)
    b16 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b16.insert(0, '0')
    # b16['state'] = DISABLED
    b16.grid(row=3, column=0, padx=3, pady=3)
    b17 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b17.insert(0, '0')
    # b17['state'] = DISABLED
    b17.grid(row=3, column=1, padx=3, pady=3)
    b18 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b18.insert(0, '0')
    # b18['state'] = DISABLED
    b18.grid(row=3, column=2, padx=3, pady=3)
    b19 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b19.insert(0, '0')
    # b19['state'] = DISABLED
    b19.grid(row=3, column=3, padx=3, pady=3)
    b20 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b20.insert(0, '0')
    # b20['state'] = DISABLED
    b20.grid(row=3, column=4, padx=3, pady=3)
    b21 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b21.insert(0, '0')
    # b21['state'] = DISABLED
    b21.grid(row=4, column=0, padx=3, pady=3)
    b22 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b22.insert(0, '0')
    # b22['state'] = DISABLED
    b22.grid(row=4, column=1, padx=3, pady=3)
    b23 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b23.insert(0, '0')
    # b23['state'] = DISABLED
    b23.grid(row=4, column=2, padx=3, pady=3)
    b24 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b24.insert(0, '0')
    # b24['state'] = DISABLED
    b24.grid(row=4, column=3, padx=3, pady=3)
    b25 = tk.Entry(opred_5, font=('Times', 15), width=2, justify=tk.CENTER)
    b25.insert(0, '0')
    # b25['state'] = DISABLED
    b25.grid(row=4, column=4, padx=3, pady=3)
    tk.Button(opred_5, text='OK', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: mas_5(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18,
                                    b19, b20, b21, b22, b23, b24, b25, opred_5)).grid(row=5, column=c, sticky='wens',
                                                                                      padx=2, pady=2)


# подсчет определителя 5*5
def mas_5(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22, b23, b24,
          b25, opred_5):
    a1 = int(b1.get())
    a2 = int(b2.get())
    a3 = int(b3.get())
    a4 = int(b4.get())
    a5 = int(b5.get())
    a6 = int(b6.get())
    a7 = int(b7.get())
    a8 = int(b8.get())
    a9 = int(b9.get())
    a10 = int(b10.get())
    a11 = int(b11.get())
    a12 = int(b12.get())
    a13 = int(b13.get())
    a14 = int(b14.get())
    a15 = int(b15.get())
    a16 = int(b16.get())
    a17 = int(b17.get())
    a18 = int(b18.get())
    a19 = int(b19.get())
    a20 = int(b20.get())
    a21 = int(b21.get())
    a22 = int(b22.get())
    a23 = int(b23.get())
    a24 = int(b24.get())
    a25 = int(b25.get())
    A = np.matrix([[a1, a2, a3, a4, a5], [a6, a7, a8, a9, a10], [a11, a12, a13, a14, a15], [a16, a17, a18, a19, a20],
                   [a21, a22, a23, a24, a25]])
    V = int(np.linalg.det(A))
    e_x = tk.Entry(opred_5, font=('Times', 15), width=10, justify=tk.LEFT, bd=0, highlightthickness=0)
    e_x.insert(0, 'V  = ')
    e_x['state'] = tk.DISABLED
    e_x.grid(row=6, column=1, columnspan=5, pady=3)
    e_xx = tk.Entry(opred_5, font=('Times', 15), width=6, justify=tk.CENTER, bd=0, highlightthickness=0)
    e_xx['state'] = tk.DISABLED
    e_xx.grid(row=5, column=2, columnspan=6, pady=3)
    e_xx['state'] = tk.NORMAL
    e_xx.delete(0, tk.END)
    e_xx.insert(0, V)
    e_xx['state'] = tk.DISABLED


# решение квадратных уравнений
def vvod_kv_ur(e1, e4, e7, koef):
    a = e1.get()
    if a == '':
        a = '1'
        e1.insert(0, '1')
    a = int(a)
    b = e4.get()
    if b == '':
        b = '1'
        e4.insert(0, '1')
    b = int(b)
    c = e7.get()
    if c == '':
        c = '0'
        e7.insert(0, '0')
    c = int(c)
    if (b ** 2 - 4 * a * c) < 0:
        e_0 = tk.Entry(koef, font=('Times', 15), width=10, justify=tk.CENTER, bd=0, highlightthickness=0)
        e_0.delete(0, tk.END)
        e_0.insert(0, 'Нет корней')
        e_0['state'] = tk.DISABLED
        e_0.config(background='#000000', disabledbackground='#f8ffff')
        e_0.grid(row=3, column=0, columnspan=7, pady=5)
        e_00 = tk.Entry(koef, font=('Times', 15), width=15, justify=tk.LEFT, bd=0, highlightthickness=0)
        e_00['state'] = tk.DISABLED
        e_00.config(background='#000000', disabledbackground='#09bd87')
        e_00.grid(row=4, column=1, columnspan=5, pady=3)
    elif (b ** 2 - 4 * a * c) == 0:
        x = (-b) / 2 * a
        e_x = tk.Entry(koef, font=('Times', 15), width=10, justify=tk.LEFT, bd=0, highlightthickness=0)
        e_x.insert(0, 'x    = ')
        e_x['state'] = tk.DISABLED
        e_x.config(background='#000000', disabledbackground='#f8ffff')
        e_x.grid(row=3, column=1, columnspan=5, pady=3)
        e_xx = tk.Entry(koef, font=('Times', 15), width=6, justify=tk.CENTER, bd=0, highlightthickness=0)
        e_xx['state'] = tk.DISABLED
        e_xx.config(background='#000000', disabledbackground='#f8ffff')
        e_xx.grid(row=3, column=2, columnspan=6, pady=3)
        e_xx['state'] = tk.NORMAL
        e_xx.delete(0, tk.END)
        e_xx.insert(0, x)
        e_xx['state'] = tk.DISABLED
        e_00 = tk.Entry(koef, font=('Times', 15), width=15, justify=tk.LEFT, bd=0, highlightthickness=0)
        e_00['state'] = tk.DISABLED
        e_00.config(background='#000000', disabledbackground='#09bd87')
        e_00.grid(row=4, column=1, columnspan=5, pady=3)
    else:
        d = b ** 2 - 4 * a * c
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        e_x1 = tk.Entry(koef, font=('Times', 15), width=10, justify=tk.LEFT, bd=0, highlightthickness=0)
        e_x1.insert(0, 'x1   = ')
        e_x1['state'] = tk.DISABLED
        e_x1.config(background='#000000', disabledbackground='#f8ffff')
        e_x1.grid(row=3, column=1, columnspan=5, pady=3)
        e_01 = tk.Entry(koef, font=('Times', 15), width=6, justify=tk.CENTER, bd=0, highlightthickness=0)
        e_01.config(background='#000000', disabledbackground='#f8ffff')
        e_01.grid(row=3, column=2, columnspan=6, pady=3)
        e_x2 = tk.Entry(koef, font=('Times', 15), width=10, justify=tk.LEFT, bd=0, highlightthickness=0)
        e_x2.insert(0, 'x2   = ')
        e_x2['state'] = tk.DISABLED
        e_x2.config(background='#000000', disabledbackground='#f8ffff')
        e_x2.grid(row=4, column=1, columnspan=5, pady=3)
        e_02 = tk.Entry(koef, font=('Times', 15), width=6, justify=tk.CENTER, bd=0, highlightthickness=0)
        e_02.config(background='#000000', disabledbackground='#f8ffff')
        e_02.grid(row=4, column=2, columnspan=6, pady=3)
        e_01.delete(0, tk.END)
        e_01.insert(0, x1)
        e_01['state'] = tk.DISABLED
        e_02.delete(0, tk.END)
        e_02.insert(0, x2)
        e_02['state'] = tk.DISABLED


# окно для ввода квадратных уравнений
def okno_kv_ur(t):
    koef = tk.Toplevel(t)
    koef.minsize(width=320, height=500)
    koef['bg'] = '#09bd87'
    koef.grid()
    koef.title('Квадратное уравнение')

    ecmd = (koef.register(validate_e), '%P')
    e1 = tk.Entry(koef, font=('Times', 15), width=2, justify=tk.CENTER, validate='key', validatecommand=ecmd)
    e1.focus()
    e1.grid(row=1, column=0, padx=3, pady=3)
    e2 = tk.Entry(koef, font=('Times', 15), width=2, justify=tk.CENTER)
    e2.insert(0, 'x²')
    e2['state'] = tk.DISABLED
    e2.grid(row=1, column=1, padx=3, pady=3)
    e3 = tk.Entry(koef, font=('Times', 15), width=2, justify=tk.CENTER)
    e3.insert(0, '+')
    e3['state'] = tk.DISABLED
    e3.grid(row=1, column=2, padx=3, pady=3)
    e4 = tk.Entry(koef, font=('Times', 15), width=2, justify=tk.CENTER, validate='key', validatecommand=ecmd)
    e4.focus()
    e4.grid(row=1, column=3, padx=3, pady=3)
    e5 = tk.Entry(koef, font=('Times', 15), width=2, justify=tk.CENTER)
    e5.insert(0, 'x')
    e5['state'] = tk.DISABLED
    e5.grid(row=1, column=4, padx=3, pady=3)
    e6 = tk.Entry(koef, font=('Times', 15), width=2, justify=tk.CENTER)
    e6.insert(0, '+')
    e6['state'] = tk.DISABLED
    e6.grid(row=1, column=5, padx=3, pady=3)
    e7 = tk.Entry(koef, font=('Times', 15), width=2, justify=tk.CENTER, validate='key', validatecommand=ecmd)
    e7.focus()
    e7.grid(row=1, column=6, padx=3, pady=3)
    tk.Button(koef, text='OK', bd=3, bg='#f0ffff', font=('Arial', 13),
              command=lambda: vvod_kv_ur(e1, e4, e7, koef)).grid(row=2, column=0,
                                                                 sticky='wens',
                                                                 padx=2, pady=2,
                                                                 columnspan=7)
    koef.mainloop()


# Ввод через клавиатуру
def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    if event.char in ['+', '-', '*', '/', '.']:
        if event.char == '*':
            event.char = '×'
        if event.char == '/':
            event.char = '÷'
        add_sign(event.char)
    if event.char in ['=', '\r']:
        equally(event.char)
    if event.char == '\x1b':
        Delete_0(event.char)
    if event.char == '\x08':
        Delete_1(event.char)
    if event.char == '`':
        Delete_2(event.char)


# Главный экран
calc = tk.Tk()
calc.title('Калькулятор')
calc['bg'] = '#09bd87'
calc.minsize(width=320, height=500)
calc.maxsize(width=320, height=500)
# Поле ввода (элементы появляются справа)
calc_etry = tk.Entry(calc, justify=tk.RIGHT, font=('Arial', 20), width=20, bd=5)
calc_etry.insert(0, '0')
calc_etry['state'] = tk.DISABLED
calc_etry.config(background='#000000', disabledbackground='#f8ffff')
calc_etry.grid(row=0, column=0, columnspan=4, sticky='we')
# Кнопки
but1 = [
    "M", "CE", "C", "⌫",
    "⅟х", "x²", "√х", "÷",
    "7", "8", "9", "×",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "±", "0", ".", "="
]
calc.bind('<Key>', press_key)
# Переменные
r, c = 1, 0
HZ = 0

for i in but1:
    if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: add_digit(v)).grid(row=r,
                                                                                                               column=c,
                                                                                                               sticky='wens',
                                                                                                               padx=2,
                                                                                                               pady=2)
    elif i in ['+', '-', '×', '÷', '.']:
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: add_sign(v)).grid(row=r,
                                                                                                              column=c,
                                                                                                              sticky='wens',
                                                                                                              padx=2,
                                                                                                              pady=2)
    elif i == '=':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: equally(v)).grid(row=r,
                                                                                                             column=c,
                                                                                                             sticky='wens',
                                                                                                             padx=2,
                                                                                                             pady=2)
    elif i == '⅟х':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: denominator(v)).grid(row=r,
                                                                                                                 column=c,
                                                                                                                 sticky='wens',
                                                                                                                 padx=2,
                                                                                                                 pady=2)
    elif i == 'x²':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: sq(v)).grid(row=r, column=c,
                                                                                                        sticky='wens',
                                                                                                        padx=2, pady=2)
    elif i == '√х':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: sq_r(v)).grid(row=r,
                                                                                                          column=c,
                                                                                                          sticky='wens',
                                                                                                          padx=2,
                                                                                                          pady=2)
    elif i == 'C':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: Delete_0(v)).grid(row=r,
                                                                                                              column=c,
                                                                                                              sticky='wens',
                                                                                                              padx=2,
                                                                                                              pady=2)
    elif i == '⌫':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: Delete_1(v)).grid(row=r,
                                                                                                              column=c,
                                                                                                              sticky='wens',
                                                                                                              padx=2,
                                                                                                              pady=2)
    elif i == 'CE':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: Delete_2(v)).grid(row=r,
                                                                                                              column=c,
                                                                                                              sticky='wens',
                                                                                                              padx=2,
                                                                                                              pady=2)
    elif i == '±':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda v=i: neg(v)).grid(row=r,
                                                                                                         column=c,
                                                                                                         sticky='wens',
                                                                                                         padx=2, pady=2)
    elif i == 'M':
        tk.Button(calc, text=i, bd=5, bg='#f0ffff', font=('Arial', 13), command=lambda: menu(calc)).grid(row=r,
                                                                                                         column=c,
                                                                                                         sticky='wens',
                                                                                                         padx=2, pady=2)
    calc.grid_rowconfigure(r, minsize=75)
    calc.grid_columnconfigure(c, minsize=70)
    c += 1
    if c > 3:
        c = 0
        r += 1
