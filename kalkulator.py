import math
import tkinter as tk
from tkinter import messagebox

import numpy as np

import starting


def validate_e(new_value):
  '''
    Ограничение ввода символов
    :param new_value: символ, который собираются ввести
    :return: ограничивает ввод неверных символов
    '''
  try:
    if new_value == "" or new_value == "-":
      return True
    _str = str(int(new_value))
    return True
  except:
    return False


def validate_k(new_value):
  '''
    Ограничение ввода символов
    :param new_value: символ, который собираются ввести
    :return: ограничивает ввод неверных символов
    '''
  try:
    if new_value == "":
      return True
    _str = str(int(new_value))
    return True
  except:
    return False


def add_magic(entry):
  '''
    проверка на ввод нужных символов действий
    :param entry: предполагаемый символ действия
    :return: либо ввод, либо отказ
    '''
  x = y = s = ''
  for i in range(len(entry)):
    if entry[i] in ['+', '-', '×', '÷']:
      x = y
      y = ''
      s = entry[i]
    else:
      y += entry[i]
  return x, y, s


def Delete_0(Del):
  '''
    стирает все, что было написано
    :param Del: -
    :return: в строке все будет стерто
    '''
  calc_etry['state'] = tk.NORMAL
  calc_etry.delete(0, tk.END)
  calc_etry.insert(0, '0')
  calc_etry['state'] = tk.DISABLED


def Delete_1(Del):
  '''
    стирает последний элемент
    :param Del: -
    :return: послежний элемент стерт
    '''
  entry = calc_etry.get()
  entry = entry[:-1]
  if len(entry) == 0:
    entry = '0'
  calc_etry['state'] = tk.NORMAL
  calc_etry.delete(0, tk.END)
  calc_etry.insert(0, entry)
  calc_etry['state'] = tk.DISABLED


def Delete_2(Del):
  '''
    стирает всё после символа операции
    :param Del: -
    :return: символы после операции стерты
    '''
  entry = calc_etry.get()
  entry_0, entry_1, sim = add_magic(entry)
  if sim == '' or entry_0 == '':
    entry = '0'
  else:
    entry = entry_0 + sim
  calc_etry['state'] = tk.NORMAL
  calc_etry.delete(0, tk.END)
  calc_etry.insert(0, entry)
  calc_etry['state'] = tk.DISABLED


def add_pl(x, y):
  '''
    складывает два числа
    :param x: первое число
    :param y: второе число
    :return: сумма чисел
    '''
  if type(x) == float and type(y) == float:
    return str(x + y)
  else:
    raise TypeError


def add_mi(x, y):
  '''
    вычитает числа
    :param x: уменьшаемое
    :param y: вычитаемое
    :return: разность
    '''
  if type(x) == float and type(y) == float:
    return str(x - y)
  else:
    raise TypeError


def add_um(x, y):
  '''
    умножает два числа
    :param x: первый множитель
    :param y: второй множитель
    :return: произведение
    '''
  if type(x) == float and type(y) == float:
    return str(x * y)
  else:
    raise TypeError


def add_de(x, y):
  '''
    делит одно число на другое
    :param x: делимое
    :param y: делитель
    :return: частное
    '''
  if type(x) == float and type(y) == float:
    try:
      return str(x / y)
    except ZeroDivisionError:

      messagebox.showerror('Ошибка', 'Деление на ноль невозможно')
      return 0
  else:
    raise TypeError


def denominator(denominator):
  '''
    Знаменатель "⅟х"
    :param denominator: -
    :return: частное 1/х
    '''
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


def sq(square):
  '''
    возводит в квадрат
    :param square: -
    :return: число в квадрате
    '''
  entry = calc_etry.get()
  global HZ
  HZ = 1
  if ('+' in entry) or ('-' in entry) or ('×' in entry) or ('÷' in entry):
    if entry[-1] in ['+', '-', '×', '÷']:
      entry = entry + entry[:-1]
    entry = add_calculation_0(entry)
  entry = float(entry)**2
  if entry == int(entry):
    entry = str(int(entry))
  calc_etry['state'] = tk.NORMAL
  calc_etry.delete(0, tk.END)
  calc_etry.insert(0, entry)
  calc_etry['state'] = tk.DISABLED


def sq_r(square_root):
  '''
    находит корень из числа
    :param square_root: -
    :return: корень из числа
    '''
  entry = calc_etry.get()
  global HZ
  HZ = 1
  if ('+' in entry) or ('-' in entry) or ('×' in entry) or ('÷' in entry):
    if entry[-1] in ['+', '-', '×', '÷']:
      entry = entry + entry[:-1]
    entry = add_calculation_0(entry)
  entry = float(entry)**0.5
  if entry == int(entry):
    entry = str(int(entry))
  calc_etry['state'] = tk.NORMAL
  calc_etry.delete(0, tk.END)
  calc_etry.insert(0, entry)
  calc_etry['state'] = tk.DISABLED


def add_calculation_1(S, x, y):
  '''
    расчет
    :param S: знак
    :param x: первое число
    :param y: второе число
    :return: действие с этими числами
    '''
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


def add_calculation_0(entry):
  '''
    Разбивает строку на 2 числа и символ между ними
    :param entry: строка
    :return: итог операции
    '''
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


def add_digit(digit):
  '''
    добавление цифры
    :param digit: что добавляем
    :return: цифра добавлена
    '''
  entry = calc_etry.get()
  global HZ
  if HZ == 1:
    entry = '0'
    HZ = 0
  if entry[0] == '0' and len(entry) == 1:
    entry = entry[1:]
  if (len(entry) > 1) and (entry[-1] == '0') and (entry[-2] in [
      '+', '-', '×', '÷'
  ]) and (digit != '.'):
    entry = entry[:-1]
  calc_etry['state'] = tk.NORMAL
  calc_etry.delete(0, tk.END)
  calc_etry.insert(0, entry + digit)
  calc_etry['state'] = tk.DISABLED


def add_sign(sing):
  '''
    добавление знака
    :param sing: что добавляем
    :return: знак добавлена
    '''
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
  if entry[-1] in ['+', '-', '×', '÷'
                   ] and ('+' in entry[:-1] or '-' in entry[:-1]
                          or '×' in entry[:-1] or '÷' in entry[:-1]):
    entry = str(add_calculation_0(entry[:-1])) + entry[-1]
  calc_etry['state'] = tk.NORMAL
  calc_etry.delete(0, tk.END)
  calc_etry.insert(0, entry)
  calc_etry['state'] = tk.DISABLED


def equally(eq):
  '''
    равно
    :param eq: ?
    :return: ?
    '''
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


def menu(calc):
  '''
    меню
    :param calc: окно для вывода результата
    :return: меню и кнопки
    '''
  menu_top = tk.Toplevel(calc)
  # menu_top.overrideredirect(True)
  menu_top['bg'] = '#09bd87'
  menu_top.minsize(width=380, height=500)
  menu_top.maxsize(width=380, height=500)
  tk.Button(menu_top,
            text='Игра',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: game(menu_top)).grid(row=0,
                                                 column=0,
                                                 sticky='wens',
                                                 padx=2,
                                                 pady=2)
  tk.Button(menu_top,
            text='Вычисление опеределителя целых чисел',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: okno_opredelit(menu_top)).grid(row=1,
                                                           column=0,
                                                           sticky='wens',
                                                           padx=2,
                                                           pady=2)
  tk.Button(menu_top,
            text='Квадратное уравнение',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: okno_kv_ur(menu_top)).grid(row=2,
                                                       column=0,
                                                       sticky='wens',
                                                       padx=2,
                                                       pady=2)
  tk.Button(menu_top,
            text='Угол между векторами',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: ugol_vector(menu_top)).grid(row=3,
                                                        column=0,
                                                        sticky='wens',
                                                        padx=2,
                                                        pady=2)
  tk.Button(menu_top,
            text='Площадь и периметр фигур',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: okno_plochad(menu_top)).grid(row=4,
                                                         column=0,
                                                         sticky='wens',
                                                         padx=2,
                                                         pady=2)


def okno_plochad(t):
  '''
    окно для выбора вида фигуры, для которой будет рассчитываться площадь
    :param t: окно для вывода результата
    :return: окно, где можно выбрать вид фигуры
    '''
  pl = tk.Toplevel(t)
  pl.minsize(width=320, height=500)
  pl['bg'] = '#09bd87'
  pl.grid()
  pl.title('Вычисление определителя')
  tk.Button(pl,
            text='Прямоугольник',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: priam(pl)).grid(row=0,
                                            column=0,
                                            sticky='wens',
                                            padx=2,
                                            pady=2)
  tk.Button(pl,
            text='Круг',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: krug(pl)).grid(row=1,
                                           column=0,
                                           sticky='wens',
                                           padx=2,
                                           pady=2)
  tk.Button(pl,
            text='Квадрат',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: kvadrat(pl)).grid(row=2,
                                              column=0,
                                              sticky='wens',
                                              padx=2,
                                              pady=2)
  tk.Button(pl,
            text='Треугольник(по 3ём сторонам)',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: treug(pl)).grid(row=3,
                                            column=0,
                                            sticky='wens',
                                            padx=2,
                                            pady=2)


def priam(pl):
  '''
            Нахождение площади и периметра прямоугольника
            :param pl: окно для создания дочернего окна
            :return: площадь и периметр прямоугольника
            '''
  S = tk.Toplevel(pl)
  S.minsize(width=400, height=200)
  S['bg'] = '#f8ffff'
  S.grid()
  S.title('Площадь прямоугольника')
  bcmd = (S.register(validate_k), '%P')
  b0 = tk.Entry(S, font=('Times', 15), width=50, justify=tk.CENTER, bd=3)
  b0.insert(0, 'Введите длины сторон')
  b0['state'] = tk.DISABLED
  b0.config(background='#000000', disabledbackground='#f8ffff')
  b0.grid(row=0, column=0, sticky='we', columnspan=4)
  b1 = tk.Entry(S, font=('Times', 15), width=30, justify=tk.LEFT, bd=3)
  b1.insert(0, 'Длина первой стороны=')
  b1['state'] = tk.DISABLED
  b1.config(background='#000000', disabledbackground='#f8ffff')
  b1.grid(row=1, column=0, sticky='wens', pady=3)
  b2 = tk.Entry(S,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b2['state'] = tk.DISABLED
  b2.grid(row=1, column=1, padx=3, pady=3, sticky='wens')
  b2.focus()
  b5 = tk.Entry(S, font=('Times', 15), width=30, justify=tk.LEFT, bd=3)
  b5.insert(0, 'Длина второй стороны=')
  b5['state'] = tk.DISABLED
  b5.config(background='#000000', disabledbackground='#f8ffff')
  b5.grid(row=2, column=0, sticky='wens', pady=3)
  b6 = tk.Entry(S,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b6['state'] = tk.DISABLED
  b6.grid(row=2, column=1, padx=3, pady=3, sticky='wens')
  b6.focus()
  tk.Button(S,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: pl_priam(b2, b6, S)).grid(row=3,
                                                      column=0,
                                                      sticky='wens',
                                                      padx=2,
                                                      pady=2,
                                                      columnspan=1)


def pl_priam(b2, b6, pl):
  '''
           Вычисление площади и периметра прямоугольника
           :param b2: сторона 1 прямоугольника
           :param b6: сторона 2 прямоугольника
           :param pl: окно вызова и вывода результат функции
           :return: площадь и периметр прямоугольника
           '''
  a1 = b2.get()
  if a1 == '':
    a1 = '0'
    b2.insert(0, '0')
  a1 = int(a1)
  a2 = b6.get()
  if a2 == '':
    a2 = '0'
    b6.insert(0, '0')
  a2 = int(a2)
  S = a1 * a2
  P = a1 * 2 + a2 * 2
  if (a1 > 0 and a2 > 0):
    e_x = tk.Entry(pl,
                   font=('Times', 15),
                   width=3,
                   justify=tk.LEFT,
                   bd=0,
                   highlightthickness=0)
    e_x.insert(0, 'S    = ')
    e_x['state'] = tk.DISABLED
    e_x.config(background='#000000', disabledbackground='#f8ffff')
    e_x.grid(row=4, column=1, columnspan=1, pady=3, sticky='wens')
    e_xx = tk.Entry(pl,
                    font=('Times', 15),
                    width=6,
                    justify=tk.CENTER,
                    bd=0,
                    highlightthickness=0)
    e_xx['state'] = tk.DISABLED
    e_xx.config(background='#000000', disabledbackground='#f8ffff')
    e_xx.grid(row=4, column=2, columnspan=1, pady=3, sticky='wens')
    e_xx['state'] = tk.NORMAL
    e_xx.delete(0, tk.END)
    e_xx.insert(0, S)
    e_xx['state'] = tk.DISABLED
    e_xxx = tk.Entry(pl,
                     font=('Times', 15),
                     width=3,
                     justify=tk.LEFT,
                     bd=0,
                     highlightthickness=0)
    e_xxx.insert(0, 'P    = ')
    e_xxx['state'] = tk.DISABLED
    e_xxx.config(background='#000000', disabledbackground='#f8ffff')
    e_xxx.grid(row=5, column=1, columnspan=1, pady=3, sticky='wens')
    e_xxxx = tk.Entry(pl,
                      font=('Times', 15),
                      width=6,
                      justify=tk.CENTER,
                      bd=0,
                      highlightthickness=0)
    e_xxxx['state'] = tk.DISABLED
    e_xxxx.config(background='#000000', disabledbackground='#f8ffff')
    e_xxxx.grid(row=5, column=2, columnspan=1, pady=3, sticky='wens')
    e_xxxx['state'] = tk.NORMAL
    e_xxxx.delete(0, tk.END)
    e_xxxx.insert(0, P)
    e_xxxx['state'] = tk.DISABLED
  elif(a1==0 or a2==0):
      e_x = tk.Entry(pl,
                     font=('Times', 15),
                     width=3,
                     justify=tk.LEFT,
                     bd=0,
                     highlightthickness=0)
      e_x.insert(0, 'Ошибка')
      e_x['state'] = tk.DISABLED
      e_x.config(background='#000000', disabledbackground='#f8ffff')
      e_x.grid(row=4, column=1, columnspan=2, pady=3, sticky='wens')
      e_xxx = tk.Entry(pl,
                       font=('Times', 15),
                       width=3,
                       justify=tk.LEFT,
                       bd=0,
                       highlightthickness=0)
      e_xxx.insert(0, 'Длинa/ы=0')
      e_xxx['state'] = tk.DISABLED
      e_xxx.config(background='#000000', disabledbackground='#f8ffff')
      e_xxx.grid(row=5, column=1, columnspan=2, pady=3, sticky='wens')


def krug(pl):
  '''
            Нахождение площади и периметра круга
            :param pl: окно для создания дочернего окна
            :return: площадь и периметр круга
            '''
  S = tk.Toplevel(pl)
  S.minsize(width=400, height=200)
  S['bg'] = '#f8ffff'
  S.grid()
  S.title('Площадь круга')
  bcmd = (S.register(validate_k), '%P')
  b0 = tk.Entry(S, font=('Times', 15), width=50, justify=tk.CENTER, bd=3)
  b0.insert(0, 'Введите длину радиуса')
  b0['state'] = tk.DISABLED
  b0.config(background='#000000', disabledbackground='#f8ffff')
  b0.grid(row=0, column=0, sticky='we', columnspan=4)
  b1 = tk.Entry(S, font=('Times', 15), width=30, justify=tk.LEFT, bd=3)
  b1.insert(0, 'Длина радиуса=')
  b1['state'] = tk.DISABLED
  b1.config(background='#000000', disabledbackground='#f8ffff')
  b1.grid(row=1, column=0, sticky='wens', pady=3)
  b2 = tk.Entry(S,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b2['state'] = tk.DISABLED
  b2.grid(row=1, column=1, padx=3, pady=3, sticky='wens')
  b2.focus()
  tk.Button(S,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: pl_krug(b2, S)).grid(row=3,
                                                 column=0,
                                                 sticky='wens',
                                                 padx=2,
                                                 pady=2,
                                                 columnspan=1)


def pl_krug(b2, pl):
  '''
           Вычисление площади и периметра круга
           :param b2: радиус круга
           :param pl: окно вызова и вывода результат функции
           :return: площадь и периметр круга
           '''
  a1 = b2.get()
  if a1 == '':
    a1 = '0'
    b2.insert(0, '0')
  a1 = int(a1)
  p = math.pi
  S = a1 * a1 * p
  P = 2 * p * a1
  e_x = tk.Entry(pl,
                 font=('Times', 15),
                 width=3,
                 justify=tk.LEFT,
                 bd=0,
                 highlightthickness=0)
  e_x.insert(0, 'S    = ')
  e_x['state'] = tk.DISABLED
  e_x.config(background='#000000', disabledbackground='#f8ffff')
  e_x.grid(row=4, column=1, columnspan=1, pady=3, sticky='wens')
  e_xx = tk.Entry(pl,
                  font=('Times', 15),
                  width=6,
                  justify=tk.CENTER,
                  bd=0,
                  highlightthickness=0)
  e_xx['state'] = tk.DISABLED
  e_xx.config(background='#000000', disabledbackground='#f8ffff')
  e_xx.grid(row=4, column=2, columnspan=1, pady=3, sticky='wens')
  e_xx['state'] = tk.NORMAL
  e_xx.delete(0, tk.END)
  e_xx.insert(0, S)
  e_xx['state'] = tk.DISABLED
  e_xxx = tk.Entry(pl,
                   font=('Times', 15),
                   width=3,
                   justify=tk.LEFT,
                   bd=0,
                   highlightthickness=0)
  e_xxx.insert(0, 'P    = ')
  e_xxx['state'] = tk.DISABLED
  e_xxx.config(background='#000000', disabledbackground='#f8ffff')
  e_xxx.grid(row=5, column=1, columnspan=1, pady=3, sticky='wens')
  e_xxxx = tk.Entry(pl,
                    font=('Times', 15),
                    width=6,
                    justify=tk.CENTER,
                    bd=0,
                    highlightthickness=0)
  e_xxxx['state'] = tk.DISABLED
  e_xxxx.config(background='#000000', disabledbackground='#f8ffff')
  e_xxxx.grid(row=5, column=2, columnspan=1, pady=3, sticky='wens')
  e_xxxx['state'] = tk.NORMAL
  e_xxxx.delete(0, tk.END)
  e_xxxx.insert(0, P)
  e_xxxx['state'] = tk.DISABLED


def kvadrat(pl):
  '''
            Нахождение площади и периметра квадрата
            :param pl: окно для создания дочернего окна
            :return: площадь и периметр квадрата
            '''
  S = tk.Toplevel(pl)
  S.minsize(width=400, height=200)
  S['bg'] = '#f8ffff'
  S.grid()
  S.title('Площадь квадрата')
  bcmd = (S.register(validate_k), '%P')
  b0 = tk.Entry(S, font=('Times', 15), width=50, justify=tk.CENTER, bd=3)
  b0.insert(0, 'Введите длину стороны')
  b0['state'] = tk.DISABLED
  b0.config(background='#000000', disabledbackground='#f8ffff')
  b0.grid(row=0, column=0, sticky='we', columnspan=4)
  b1 = tk.Entry(S, font=('Times', 15), width=20, justify=tk.LEFT, bd=3)
  b1.insert(0, 'Длина стороны=')
  b1['state'] = tk.DISABLED
  b1.config(background='#000000', disabledbackground='#f8ffff')
  b1.grid(row=1, column=0, sticky='wens', pady=3)
  b2 = tk.Entry(S,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b2['state'] = tk.DISABLED
  b2.grid(row=1, column=1, padx=3, pady=3, sticky='wens')
  b2.focus()
  tk.Button(S,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: pl_kvadr(b2, S)).grid(row=3,
                                                  column=0,
                                                  sticky='wens',
                                                  padx=2,
                                                  pady=2,
                                                  columnspan=1)


def pl_kvadr(b2, pl):
  '''
          Вычисление площади и пермиетра квадрата
          :param b2: сторона квадрата
          :param pl: окно вызова и вывода результат функции
          :return: площадь и периметр квадрата
          '''
  a1 = b2.get()
  if a1 == '':
    a1 = '0'
    b2.insert(0, '0')
  a1 = int(a1)
  S = a1 * a1
  P = a1 * 4

  e_x = tk.Entry(pl,
                 font=('Times', 15),
                 width=3,
                 justify=tk.LEFT,
                 bd=0,
                 highlightthickness=0)
  e_x.insert(0, 'S    = ')
  e_x['state'] = tk.DISABLED
  e_x.config(background='#000000', disabledbackground='#f8ffff')
  e_x.grid(row=4, column=1, columnspan=1, pady=3, sticky='wens')
  e_xx = tk.Entry(pl,
                  font=('Times', 15),
                  width=6,
                  justify=tk.CENTER,
                  bd=0,
                  highlightthickness=0)
  e_xx['state'] = tk.DISABLED
  e_xx.config(background='#000000', disabledbackground='#f8ffff')
  e_xx.grid(row=4, column=2, columnspan=1, pady=3, sticky='wens')
  e_xx['state'] = tk.NORMAL
  e_xx.delete(0, tk.END)
  e_xx.insert(0, S)
  e_xx['state'] = tk.DISABLED
  e_xxx = tk.Entry(pl,
                   font=('Times', 15),
                   width=3,
                   justify=tk.LEFT,
                   bd=0,
                   highlightthickness=0)
  e_xxx.insert(0, 'P    = ')
  e_xxx['state'] = tk.DISABLED
  e_xxx.config(background='#000000', disabledbackground='#f8ffff')
  e_xxx.grid(row=5, column=1, columnspan=1, pady=3, sticky='wens')
  e_xxxx = tk.Entry(pl,
                    font=('Times', 15),
                    width=6,
                    justify=tk.CENTER,
                    bd=0,
                    highlightthickness=0)
  e_xxxx['state'] = tk.DISABLED
  e_xxxx.config(background='#000000', disabledbackground='#f8ffff')
  e_xxxx.grid(row=5, column=2, columnspan=1, pady=3, sticky='wens')
  e_xxxx['state'] = tk.NORMAL
  e_xxxx.delete(0, tk.END)
  e_xxxx.insert(0, P)
  e_xxxx['state'] = tk.DISABLED


def treug(pl):
  '''
        Нахождение площади и периметра треугольника
        :param pl: окно для создания дочернего окна
        :return: площадь и периметр треугольника
        '''
  S = tk.Toplevel(pl)
  S.minsize(width=400, height=200)
  S['bg'] = '#f8ffff'
  S.grid()
  S.title('Площадь треугольника')
  bcmd = (S.register(validate_k), '%P')
  b0 = tk.Entry(S, font=('Times', 15), width=50, justify=tk.CENTER, bd=3)
  b0.insert(0, 'Введите длины сторон')
  b0['state'] = tk.DISABLED
  b0.config(background='#000000', disabledbackground='#f8ffff')
  b0.grid(row=0, column=0, sticky='we', columnspan=4)
  b1 = tk.Entry(S, font=('Times', 15), width=3, justify=tk.CENTER, bd=3)
  b1.insert(0, 'A')
  b1['state'] = tk.DISABLED
  b1.config(background='#000000', disabledbackground='#f8ffff')
  b1.grid(row=1, column=0, sticky='wens', pady=3)
  b2 = tk.Entry(S,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b2['state'] = tk.DISABLED
  b2.grid(row=1, column=1, padx=3, pady=3, sticky='wens')
  b2.focus()
  b5 = tk.Entry(S, font=('Times', 15), width=3, justify=tk.CENTER, bd=3)
  b5.insert(0, 'B')
  b5['state'] = tk.DISABLED
  b5.config(background='#000000', disabledbackground='#f8ffff')
  b5.grid(row=2, column=0, sticky='wens', pady=3)
  b6 = tk.Entry(S,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b6['state'] = tk.DISABLED
  b6.grid(row=2, column=1, padx=3, pady=3, sticky='wens')
  b6.focus()
  b7 = tk.Entry(S, font=('Times', 15), width=3, justify=tk.CENTER, bd=3)
  b7.insert(0, 'C')
  b7['state'] = tk.DISABLED
  b7.config(background='#000000', disabledbackground='#f8ffff')
  b7.grid(row=3, column=0, sticky='wens', pady=3)
  b8 = tk.Entry(S,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b8['state'] = tk.DISABLED
  b8.grid(row=3, column=1, padx=3, pady=3, sticky='wens')
  b8.focus()
  tk.Button(S,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: pl_treug(b2, b6, b8, S)).grid(row=4,
                                                          column=0,
                                                          sticky='wens',
                                                          padx=2,
                                                          pady=2,
                                                          columnspan=2)


def pl_treug(b2, b6, b8, pl):
  '''
        Вычисление площади и периметра треугольника
        :param b1: сторона 1 треугольника
        :param b6: сторона 2 треугольника
        :param b8: сторона 3 треугольника
        :param pl: окно вызова и вывода результат функции
        :return: площадь и периметр треугольника
        '''
  a1 = b2.get()
  if a1 == '':
    a1 = '0'
    b2.insert(0, '0')
  a1 = int(a1)
  a2 = b6.get()
  if a2 == '':
    a2 = '0'
    b6.insert(0, '0')
  a2 = int(a2)
  a3 = b8.get()
  if a3 == '':
    a3 = '0'
    b8.insert(0, '0')
  a3 = int(a3)
  if (a1 + a2 <= a3 or a1 + a3 <= a2 or a2 + a3 <= a1):
    #
    e_xx = tk.Entry(pl,
                    font=('Times', 13),
                    width=30,
                    justify=tk.CENTER,
                    bd=0,
                    highlightthickness=0)
    e_xx.insert(0, 'Ошибка')
    e_xx['state'] = tk.DISABLED
    e_xx.config(background='#000000', disabledbackground='#f8ffff')
    e_xx.grid(row=5, column=0, columnspan=2, pady=3, sticky='wens')
    e_xxxx = tk.Entry(pl,
                      font=('Times', 13),
                      width=30,
                      justify=tk.CENTER,
                      bd=0,
                      highlightthickness=0)
    e_xxxx.insert(0, 'Такого треугольника не существует')
    e_xxxx['state'] = tk.DISABLED
    e_xxxx.config(background='#000000', disabledbackground='#f8ffff')
    e_xxxx.grid(row=6, column=0, columnspan=2, pady=3, sticky='wens')
  else:
    p = (a1 + a2 + a3) * 0.5
    k = p * (p - a1) * (p - a2) * (p - a3)
    S = k**0.5
    P = a1 + a2 + a3
    e_x = tk.Entry(pl,
                   font=('Times', 13),
                   width=1,
                   justify=tk.LEFT,
                   bd=0,
                   highlightthickness=0)
    e_x.insert(0, 'Площадь: ')
    e_x['state'] = tk.DISABLED
    e_x.config(background='#000000', disabledbackground='#f8ffff')
    e_x.grid(row=5, column=0, pady=3, sticky='wens', columnspan=1)
    e_xx = tk.Entry(pl,
                    font=('Times', 13),
                    width=6,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_xx['state'] = tk.DISABLED
    e_xx.config(background='#000000', disabledbackground='#f8ffff')
    e_xx.grid(row=5, column=1, pady=3, sticky='wens', columnspan=2)
    e_xx['state'] = tk.NORMAL
    e_xx.delete(0, tk.END)
    e_xx.insert(0, S)
    e_xx['state'] = tk.DISABLED
    e_xxx = tk.Entry(pl,
                     font=('Times', 13),
                     width=1,
                     justify=tk.LEFT,
                     bd=0,
                     highlightthickness=0)
    e_xxx.insert(0, 'Периметр: ')
    e_xxx['state'] = tk.DISABLED
    e_xxx.config(background='#000000', disabledbackground='#f8ffff')
    e_xxx.grid(row=6, column=0, pady=3, sticky='wens', columnspan=1)
    e_xxxx = tk.Entry(pl,
                      font=('Times', 13),
                      width=6,
                      justify=tk.LEFT,
                      bd=0,
                      highlightthickness=0)
    e_xxxx['state'] = tk.DISABLED
    e_xxxx.config(background='#f8ffff', disabledbackground='#f8ffff')
    e_xxxx.grid(row=6, column=1, pady=3, sticky='wens', columnspan=2)
    e_xxxx['state'] = tk.NORMAL
    e_xxxx.delete(0, tk.END)
    e_xxxx.insert(0, P)
    e_xxxx['state'] = tk.DISABLED


def ugol_vector(t):
  '''
    Нахождение угла между векторами
    :param t: окно для вывода результата
    :return: угол между векторами
    '''
  ugol = tk.Toplevel(t)
  ugol.minsize(width=400, height=200)
  ugol['bg'] = '#f8ffff'
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
  b2 = tk.Entry(ugol,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b2['state'] = tk.DISABLED
  b2.grid(row=1, column=1, padx=3, pady=3, sticky='wens')
  b2.focus()
  b3 = tk.Entry(ugol,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b3['state'] = tk.DISABLED
  b3.grid(row=1, column=2, padx=3, pady=3, sticky='wens')
  b3.focus()
  b4 = tk.Entry(ugol,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b4['state'] = DISABLED
  b4.grid(row=1, column=3, padx=3, pady=3, sticky='wens')
  b4.focus()
  b5 = tk.Entry(ugol, font=('Times', 15), width=30, justify=tk.LEFT, bd=3)
  b5.insert(0, 'Координаты 2ого вектора:')
  b5['state'] = tk.DISABLED
  b5.config(background='#000000', disabledbackground='#f8ffff')
  b5.grid(row=2, column=0, sticky='wens', pady=3)
  b6 = tk.Entry(ugol,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b6['state'] = tk.DISABLED
  b6.grid(row=2, column=1, padx=3, pady=3, sticky='wens')
  b6.focus()
  b7 = tk.Entry(ugol,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b7['state'] = DISABLED
  b7.grid(row=2, column=2, padx=3, pady=3, sticky='wens')
  b7.focus()
  b8 = tk.Entry(ugol,
                font=('Times', 15),
                width=2,
                justify=tk.CENTER,
                bd=5,
                bg='#f8ffff',
                validate='key',
                validatecommand=bcmd)
  # b8['state'] = DISABLED
  b8.grid(row=2, column=3, padx=3, pady=3, sticky='wens')
  b8.focus()
  tk.Button(ugol,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: Ugol2(b2, b3, b4, b6, b7, b8, ugol)).grid(
              row=3, column=0, sticky='wens', padx=2, pady=2, columnspan=1)


def Ugol2(b2, b3, b4, b6, b7, b8, ugol):
  '''
    подсчет и вывод угла в градусах
    :param b2: координата x вектора 1
    :param b3: координата y вектора 1
    :param b4: координата z вектора 1
    :param b6: координата x вектора 2
    :param b7: координата y вектора 2
    :param b8: координата z вектора 2
    :param ugol:
    :return: угол между векторами
    '''
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
  ugolR = (np.arccos(
    (np.matmul(a, b_transp)) / (np.linalg.norm(a) * np.linalg.norm(b))))
  ugolG = (ugolR) * 180 / p
  t = np.round(ugolG, 2)
  q = str(t)
  q = q.replace('[', '')
  q = q.replace(']', '')
  q = q.replace('.', '°')
  e_x = tk.Entry(ugol,
                 font=('Times', 15),
                 width=3,
                 justify=tk.LEFT,
                 bd=0,
                 highlightthickness=0)
  e_x.insert(0, '⍺      = ')
  e_x['state'] = tk.DISABLED
  e_x.config(background='#000000', disabledbackground='#f8ffff')
  e_x.grid(row=4, column=1, columnspan=1, pady=3, sticky='wens')
  e_xx = tk.Entry(ugol,
                  font=('Times', 15),
                  width=6,
                  justify=tk.CENTER,
                  bd=0,
                  highlightthickness=0)
  e_xx['state'] = tk.DISABLED
  e_xx.config(background='#000000', disabledbackground='#f8ffff')
  e_xx.grid(row=4, column=2, columnspan=1, pady=3, sticky='wens')
  e_xx['state'] = tk.NORMAL
  e_xx.delete(0, tk.END)
  e_xx.insert(0, q)
  e_xx['state'] = tk.DISABLED


def okno_opredelit(t):
  '''
    окно для выбора размера определителя
    :param t: окно для вывода результата
    :return: окно, где можно выбрать размер матрицы
    '''
  matr1 = tk.Toplevel(t)
  matr1.minsize(width=320, height=500)
  matr1['bg'] = '#09bd87'
  matr1.grid()
  matr1.title('Вычисление определителя')
  tk.Button(matr1,
            text='2*2',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: opred2(matr1)).grid(row=0,
                                                column=0,
                                                sticky='wens',
                                                padx=2,
                                                pady=2)
  tk.Button(matr1,
            text='3*3',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: opred3(matr1)).grid(row=1,
                                                column=0,
                                                sticky='wens',
                                                padx=2,
                                                pady=2)
  tk.Button(matr1,
            text='4*4',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: opred4(matr1)).grid(row=2,
                                                column=0,
                                                sticky='wens',
                                                padx=2,
                                                pady=2)
  tk.Button(matr1,
            text='5*5',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: opred5(matr1)).grid(row=3,
                                                column=0,
                                                sticky='wens',
                                                padx=2,
                                                pady=2)


def game(t):
  '''
    запуск игры
    :param t: полотно
    :return: рабочая игра
    '''
  starting.go()


def opred2(t):
  '''
       ввод определителя 2*2
       :param t: -
       :return: вычисление определителя
       '''
  opred_2 = tk.Toplevel(t)
  opred_2.minsize(width=320, height=320)
  opred_2['bg'] = '#f8ffff'
  opred_2.grid()
  opred_2.title('Определитель 2*2')
  mcmd = (opred_2.register(validate_e), '%P')
  b1 = tk.Entry(opred_2,
                font=('Times', 15),
                width=6,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b1.grid(row=0, column=0, padx=3, pady=3, sticky='wens')
  b2 = tk.Entry(opred_2,
                font=('Times', 15),
                width=6,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b2.grid(row=0, column=1, padx=3, pady=3, sticky='wens')
  b3 = tk.Entry(opred_2,
                font=('Times', 15),
                width=6,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b3.grid(row=1, column=0, padx=3, pady=3, sticky='wens')
  b4 = tk.Entry(opred_2,
                font=('Times', 15),
                width=6,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b4.grid(row=1, column=1, padx=3, pady=3, sticky='wens')
  tk.Button(opred_2,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: mas_2(b1, b2, b3, b4, opred_2)).grid(row=2,
                                                                 column=0,
                                                                 sticky='wens',
                                                                 padx=2,
                                                                 pady=3,
                                                                 columnspan=1)


#подсчет определителя 2*2
def mas_2(b1, b2, b3, b4, opred_2):
  '''
       подсчет определителя 2*2
       :param b1: первое число
       :param b2: второе число
       :param b3: третье число
       :param b4: четвертое число
       :param opred_2: ?
       :return: определитель подсчитан
       '''
  a1 = b1.get()
  if a1 == '' or a1 == '-':
    a1 = '0'
    b1.delete(0, tk.END)
    b1.insert(0, '0')
  a1 = int(a1)
  a2 = b2.get()
  if a2 == '' or a2 == '-':
    a2 = '0'
    b2.delete(0, tk.END)
    b2.insert(0, '0')
  a2 = int(a2)
  a3 = b3.get()
  if a3 == '' or a3 == '-':
    a3 = '0'
    b3.delete(0, tk.END)
    b3.insert(0, '0')
  a3 = int(a3)
  a4 = b4.get()
  if a4 == '' or a4 == '-':
    a4 = '0'
    b4.delete(0, tk.END)
    b4.insert(0, '0')
  a4 = int(a4)
  A = np.matrix([[a1, a2], [a3, a4]])
  V = round(np.linalg.det(A))
  e_xx = tk.Entry(opred_2,
                  font=('Times', 15),
                  width=35,
                  justify=tk.CENTER,
                  bd=0,
                  highlightthickness=0)
  e_xx['state'] = tk.DISABLED
  e_xx.grid(row=3, column=0, columnspan=5, pady=3)
  e_xx['state'] = tk.NORMAL
  e_xx.delete(0, tk.END)
  e_xx.insert(0, V)
  e_xx['state'] = tk.DISABLED


def opred3(t):
  '''
    ввод определителя 3*3
    :param t: -
    :return: определитель 3*3
    '''
  opred_3 = tk.Toplevel(t)
  opred_3.minsize(width=320, height=320)
  opred_3['bg'] = '#09bd87'
  opred_3.grid()
  opred_3.title('Определитель 3*3')
  mcmd = (opred_3.register(validate_e), '%P')
  b1 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b1.insert(0, '0')
  # b1['state'] = DISABLED
  b1.grid(row=0, column=0, padx=3, pady=3)
  b2 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b2.insert(0, '0')
  # b2['state'] = tk.DISABLED
  b2.grid(row=0, column=1, padx=3, pady=3)
  b3 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b3.insert(0, '0')
  # b3['state'] = tk.DISABLED
  b3.grid(row=0, column=2, padx=3, pady=3)
  b4 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b4.insert(0, '0')
  # b4['state'] = DISABLED
  b4.grid(row=1, column=0, padx=3, pady=3)
  b5 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b5.insert(0, '0')
  # b5['state'] = DISABLED
  b5.grid(row=1, column=1, padx=3, pady=3)
  b6 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b6.insert(0, '0')
  # b6['state'] = tk.DISABLED
  b6.grid(row=1, column=2, padx=3, pady=3)
  b7 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b7.insert(0, '0')
  # b7['state'] = tk.DISABLED
  b7.grid(row=2, column=0, padx=3, pady=3)
  b8 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b8.insert(0, '0')
  # b8['state'] = DISABLED
  b8.grid(row=2, column=1, padx=3, pady=3)
  b9 = tk.Entry(opred_3,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b9.insert(0, '0')
  # b9['state'] = DISABLED
  b9.grid(row=2, column=2, padx=3, pady=3)
  tk.Button(
    opred_3,
    text='OK',
    bd=3,
    bg='#f0ffff',
    font=('Arial', 13),
    command=lambda: mas_3(b1, b2, b3, b4, b5, b6, b7, b8, b9, opred_3)).grid(
      row=3, column=c, sticky='wens', padx=2, pady=2)


def mas_3(b1, b2, b3, b4, b5, b6, b7, b8, b9, opred_3):
  '''
    подсчет определителя 3*3
    :param b1: р
    :param b2: а
    :param b3: з  ч
    :param b4: л  и
    :param b5: и  с
    :param b6: ч  л
    :param b7: н  а
    :param b8: ы
    :param b9: е
    :param opred_3:
    :return: определитель 3*3
    '''
  a1 = b1.get()
  if a1 == '' or a1 == '-':
    a1 = '0'
    b1.delete(0, tk.END)
    b1.insert(0, '0')
  a1 = int(a1)
  a2 = b2.get()
  if a2 == '' or a2 == '-':
    a2 = '0'
    b2.delete(0, tk.END)
    b2.insert(0, '0')
  a2 = int(a2)
  a3 = b3.get()
  if a3 == '' or a3 == '-':
    a3 = '0'
    b3.delete(0, tk.END)
    b3.insert(0, '0')
  a3 = int(a3)
  a4 = b4.get()
  if a4 == '' or a4 == '-':
    a4 = '0'
    b4.delete(0, tk.END)
    b4.insert(0, '0')
  a4 = int(a4)
  a5 = b5.get()
  if a5 == '' or a5 == '-':
    a5 = '0'
    b5.delete(0, tk.END)
    b5.insert(0, '0')
  a5 = int(a5)
  a6 = b6.get()
  if a6 == '' or a6 == '-':
    a6 = '0'
    b6.delete(0, tk.END)
    b6.insert(0, '0')
  a6 = int(a6)
  a7 = b7.get()
  if a7 == '' or a7 == '-':
    a7 = '0'
    b7.delete(0, tk.END)
    b7.insert(0, '0')
  a7 = int(a7)
  a8 = b8.get()
  if a8 == '' or a8 == '-':
    a8 = '0'
    b8.delete(0, tk.END)
    b8.insert(0, '0')
  a8 = int(a8)
  a9 = b9.get()
  if a9 == '' or a9 == '-':
    a9 = '0'
    b9.delete(0, tk.END)
    b9.insert(0, '0')
  a9 = int(a9)
  A = np.matrix([[a1, a2, a3], [a4, a5, a6], [a7, a8, a9]])
  V = round(np.linalg.det(A))
  e_xx = tk.Entry(opred_3,
                  font=('Times', 15),
                  width=40,
                  justify=tk.CENTER,
                  bd=0,
                  highlightthickness=0)
  e_xx['state'] = tk.DISABLED
  e_xx.grid(row=5, column=0, columnspan=5, pady=3)
  e_xx['state'] = tk.NORMAL
  e_xx.delete(0, tk.END)
  e_xx.insert(0, V)
  e_xx['state'] = tk.DISABLED


def opred4(t):
  '''
    ввод определителя 4*4
    :param t: &
    :return: ввод определителя 4*4
    '''
  opred_4 = tk.Toplevel(t)
  opred_4.minsize(width=320, height=320)
  opred_4['bg'] = '#09bd87'
  opred_4.grid()
  opred_4.title('Определитель 4*4')
  mcmd = (opred_4.register(validate_e), '%P')
  b1 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b1.insert(0, '0')
  # b1['state'] = DISABLED
  b1.grid(row=0, column=0, padx=3, pady=3)
  b2 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b2.insert(0, '0')
  # b2['state'] = tk.DISABLED
  b2.grid(row=0, column=1, padx=3, pady=3)
  b3 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b3.insert(0, '0')
  # b3['state'] = tk.DISABLED
  b3.grid(row=0, column=2, padx=3, pady=3)
  b4 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b4.insert(0, '0')
  # b4['state'] = DISABLED
  b4.grid(row=0, column=3, padx=3, pady=3)
  b5 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b5.insert(0, '0')
  # b5['state'] = DISABLED
  b5.grid(row=1, column=0, padx=3, pady=3)
  b6 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b6.insert(0, '0')
  # b6['state'] = tk.DISABLED
  b6.grid(row=1, column=1, padx=3, pady=3)
  b7 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b7.insert(0, '0')
  # b7['state'] = tk.DISABLED
  b7.grid(row=1, column=2, padx=3, pady=3)
  b8 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b8.insert(0, '0')
  # b8['state'] = DISABLED
  b8.grid(row=1, column=3, padx=3, pady=3)
  b9 = tk.Entry(opred_4,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b9.insert(0, '0')
  # b9['state'] = DISABLED
  b9.grid(row=2, column=0, padx=3, pady=3)
  b10 = tk.Entry(opred_4,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b10.insert(0, '0')
  # b10['state'] = DISABLED
  b10.grid(row=2, column=1, padx=3, pady=3)
  b11 = tk.Entry(opred_4,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b11.insert(0, '0')
  # b11['state'] = DISABLED
  b11.grid(row=2, column=2, padx=3, pady=3)
  b12 = tk.Entry(opred_4,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b12.insert(0, '0')
  # b12['state'] = DISABLED
  b12.grid(row=2, column=3, padx=3, pady=3)
  b13 = tk.Entry(opred_4,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b13.insert(0, '0')
  # b13['state'] = DISABLED
  b13.grid(row=3, column=0, padx=3, pady=3)
  b14 = tk.Entry(opred_4,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b14.insert(0, '0')
  # b14['state'] = DISABLED
  b14.grid(row=3, column=1, padx=3, pady=3)
  b15 = tk.Entry(opred_4,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b15.insert(0, '0')
  # b15['state'] = DISABLED
  b15.grid(row=3, column=2, padx=3, pady=3)
  b16 = tk.Entry(opred_4,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b16.insert(0, '0')
  # b16['state'] = DISABLED
  b16.grid(row=3, column=3, padx=3, pady=3)
  tk.Button(opred_4,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: mas_4(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11,
                                  b12, b13, b14, b15, b16, opred_4)).grid(
                                    row=4,
                                    column=c,
                                    sticky='wens',
                                    padx=2,
                                    pady=2)


def mas_4(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15,
          b16, opred_4):
  '''
    подсчет определителя 4*4
    :param b1:
    :param b2:
    :param b3:   р
    :param b4:   а
    :param b5:   з
    :param b6:   л
    :param b7:   и
    :param b8:   ч
    :param b9:   н   ч
    :param b10:  ы   и
    :param b11:  е   с
    :param b12:      л
    :param b13:      а
    :param b14:
    :param b15:
    :param b16:
    :param opred_4: ?
    :return: определитель 4*4
    '''
  a1 = b1.get()
  if a1 == '' or a1 == '-':
    a1 = '0'
    b1.delete(0, tk.END)
    b1.insert(0, '0')
  a1 = int(a1)

  a2 = b2.get()
  if a2 == '' or a2 == '-':
    a2 = '0'
    b2.delete(0, tk.END)
    b2.insert(0, '0')
  a2 = int(a2)

  a3 = b3.get()
  if a3 == '' or a3 == '-':
    a3 = '0'
    b3.delete(0, tk.END)
    b3.insert(0, '0')
  a3 = int(a3)

  a4 = b4.get()

  if a4 == '' or a4 == '-':
    a4 = '0'
    b4.insert(0, '0')
    b4.delete(0, tk.END)
  a4 = int(a4)

  a5 = b5.get()

  if a5 == '' or a5 == '-':
    a5 = '0'
    b5.insert(0, '0')
    b5.delete(0, tk.END)
  a5 = int(a5)

  a6 = b6.get()

  if a6 == '' or a6 == '-':
    a6 = '0'
    b6.insert(0, '0')
    b6.delete(0, tk.END)
  a6 = int(a6)

  a7 = b7.get()
  if a7 == '' or a7 == '-':
    a7 = '0'
    b7.delete(0, tk.END)
    b7.insert(0, '0')
  a7 = int(a7)

  a8 = b8.get()

  if a8 == '' or a8 == '-':
    a8 = '0'
    b8.delete(0, tk.END)
    b8.insert(0, '0')
  a8 = int(a8)

  a9 = b9.get()

  if a9 == '' or a9 == '-':
    a9 = '0'
    b9.delete(0, tk.END)
    b9.insert(0, '0')
  a9 = int(a9)

  a10 = b10.get()

  if a10 == '' or a10 == '-':
    a10 = '0'
    b10.delete(0, tk.END)
    b10.insert(0, '0')
  a10 = int(a10)

  a11 = b11.get()

  if a11 == '' or a11 == '-':
    a11 = '0'
    b11.delete(0, tk.END)
    b11.insert(0, '0')

  a11 = int(a11)

  a12 = b12.get()

  if a12 == '' or a12 == '-':
    a12 = '0'
    b12.delete(0, tk.END)
    b12.insert(0, '0')
  a12 = int(a12)

  a13 = b13.get()

  if a13 == '' or a13 == '-':
    a13 = '0'
    b13.delete(0, tk.END)
    b13.insert(0, '0')
  a13 = int(a13)

  a14 = b14.get()

  if a14 == '' or a14 == '-':
    a14 = '0'
    b14.delete(0, tk.END)
    b14.insert(0, '0')
  a14 = int(a14)

  a15 = b15.get()

  if a15 == '' or a15 == '-':
    a15 = '0'
    b15.delete(0, tk.END)
    b15.insert(0, '0')
  a15 = int(a15)

  a16 = b16.get()

  if a16 == '' or a16 == '-':
    a16 = '0'
    b16.delete(0, tk.END)
    b16.insert(0, '0')
  a16 = int(a16)
  A = np.matrix([[a1, a2, a3, a4], [a5, a6, a7, a8], [a9, a10, a11, a12],
                 [a13, a14, a15, a16]])
  V = round(np.linalg.det(A))
  e_xx = tk.Entry(opred_4,
                  font=('Times', 15),
                  width=40,
                  justify=tk.CENTER,
                  bd=0,
                  highlightthickness=0)
  e_xx['state'] = tk.DISABLED
  e_xx.grid(row=5, column=0, columnspan=5, pady=3)
  e_xx['state'] = tk.NORMAL
  e_xx.delete(0, tk.END)
  e_xx.insert(0, V)
  e_xx['state'] = tk.DISABLED


def opred5(t):
  '''
    ввод определителя 5*5
    :param t: ?
    :return: ввод определителя 5*5
    '''
  opred_5 = tk.Toplevel(t)
  opred_5.minsize(width=320, height=320)
  opred_5['bg'] = '#09bd87'
  opred_5.grid()
  opred_5.title('Определитель 5*5')
  mcmd = (opred_5.register(validate_e), '%P')
  b1 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b1.insert(0, '0')
  # b1['state'] = DISABLED
  b1.grid(row=0, column=0, padx=3, pady=3)
  b2 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b2.insert(0, '0')
  # b2['state'] = tk.DISABLED
  b2.grid(row=0, column=1, padx=3, pady=3)
  b3 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b3.insert(0, '0')
  # b3['state'] = tk.DISABLED
  b3.grid(row=0, column=2, padx=3, pady=3)
  b4 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b4.insert(0, '0')
  # b4['state'] = DISABLED
  b4.grid(row=0, column=3, padx=3, pady=3)
  b5 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b5.insert(0, '0')
  # b5['state'] = DISABLED
  b5.grid(row=0, column=4, padx=3, pady=3)
  b6 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b6.insert(0, '0')
  # b6['state'] = tk.DISABLED
  b6.grid(row=1, column=0, padx=3, pady=3)
  b7 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b7.insert(0, '0')
  # b7['state'] = tk.DISABLED
  b7.grid(row=1, column=1, padx=3, pady=3)
  b8 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b8.insert(0, '0')
  # b8['state'] = DISABLED
  b8.grid(row=1, column=2, padx=3, pady=3)
  b9 = tk.Entry(opred_5,
                font=('Times', 15),
                width=7,
                justify=tk.CENTER,
                validate='key',
                validatecommand=mcmd)
  b9.insert(0, '0')
  # b9['state'] = DISABLED
  b9.grid(row=1, column=3, padx=3, pady=3)
  b10 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b10.insert(0, '0')
  # b10['state'] = DISABLED
  b10.grid(row=1, column=4, padx=3, pady=3)
  b11 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b11.insert(0, '0')
  # b11['state'] = DISABLED
  b11.grid(row=2, column=0, padx=3, pady=3)
  b12 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b12.insert(0, '0')
  # b12['state'] = DISABLED
  b12.grid(row=2, column=1, padx=3, pady=3)
  b13 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b13.insert(0, '0')
  # b13['state'] = DISABLED
  b13.grid(row=2, column=2, padx=3, pady=3)
  b14 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b14.insert(0, '0')
  # b14['state'] = DISABLED
  b14.grid(row=2, column=3, padx=3, pady=3)
  b15 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b15.insert(0, '0')
  # b15['state'] = DISABLED
  b15.grid(row=2, column=4, padx=3, pady=3)
  b16 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b16.insert(0, '0')
  # b16['state'] = DISABLED
  b16.grid(row=3, column=0, padx=3, pady=3)
  b17 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b17.insert(0, '0')
  # b17['state'] = DISABLED
  b17.grid(row=3, column=1, padx=3, pady=3)
  b18 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b18.insert(0, '0')
  # b18['state'] = DISABLED
  b18.grid(row=3, column=2, padx=3, pady=3)
  b19 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b19.insert(0, '0')
  # b19['state'] = DISABLED
  b19.grid(row=3, column=3, padx=3, pady=3)
  b20 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b20.insert(0, '0')
  # b20['state'] = DISABLED
  b20.grid(row=3, column=4, padx=3, pady=3)
  b21 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b21.insert(0, '0')
  # b21['state'] = DISABLED
  b21.grid(row=4, column=0, padx=3, pady=3)
  b22 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b22.insert(0, '0')
  # b22['state'] = DISABLED
  b22.grid(row=4, column=1, padx=3, pady=3)
  b23 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b23.insert(0, '0')
  # b23['state'] = DISABLED
  b23.grid(row=4, column=2, padx=3, pady=3)
  b24 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b24.insert(0, '0')
  # b24['state'] = DISABLED
  b24.grid(row=4, column=3, padx=3, pady=3)
  b25 = tk.Entry(opred_5,
                 font=('Times', 15),
                 width=7,
                 justify=tk.CENTER,
                 validate='key',
                 validatecommand=mcmd)
  b25.insert(0, '0')
  # b25['state'] = DISABLED
  b25.grid(row=4, column=4, padx=3, pady=3)
  tk.Button(opred_5,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: mas_5(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11,
                                  b12, b13, b14, b15, b16, b17, b18, b19, b20,
                                  b21, b22, b23, b24, b25, opred_5)).grid(
                                    row=5,
                                    column=c,
                                    sticky='wens',
                                    padx=2,
                                    pady=2)


def mas_5(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15,
          b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, opred_5):
  '''
    подсчет определителя 5*5
    :param b1:
    :param b2:
    :param b3:
    :param b4:
    :param b5:      ЭТО ВСЕ РАЗЛИЧНЫЕ ЧИСЛА
    :param b6:
    :param b7:
    :param b8:
    :param b9:
    :param b10:    ЭТО ВСЕ РАЗЛИЧНЫЕ ЧИСЛА
    :param b11:
    :param b12:
    :param b13:
    :param b14:
    :param b15:
    :param b16:
    :param b17:
    :param b18:    ЭТО ВСЕ РАЗЛИЧНЫЕ ЧИСЛА
    :param b19:
    :param b20:
    :param b21:
    :param b22:
    :param b23:
    :param b24:
    :param b25:
    :param opred_5:
    :return: определитель 5*5
    '''
  a1 = b1.get()
  if a1 == '' or a1 == '-':
    a1 = '0'
    b1.delete(0, tk.END)
    b1.insert(0, '0')
  a1 = int(a1)

  a2 = b2.get()
  if a2 == '' or a2 == '-':
    a2 = '0'
    b2.delete(0, tk.END)
    b2.insert(0, '0')
  a2 = int(a2)

  a3 = b3.get()
  if a3 == '' or a3 == '-':
    a3 = '0'
    b3.delete(0, tk.END)
    b3.insert(0, '0')
  a3 = int(a3)

  a4 = b4.get()

  if a4 == '' or a4 == '-':
    a4 = '0'
    b4.insert(0, '0')
    b4.delete(0, tk.END)
  a4 = int(a4)

  a5 = b5.get()

  if a5 == '' or a5 == '-':
    a5 = '0'
    b5.insert(0, '0')
    b5.delete(0, tk.END)
  a5 = int(a5)

  a6 = b6.get()

  if a6 == '' or a6 == '-':
    a6 = '0'
    b6.insert(0, '0')
    b6.delete(0, tk.END)
  a6 = int(a6)

  a7 = b7.get()
  if a7 == '' or a7 == '-':
    a7 = '0'
    b7.delete(0, tk.END)
    b7.insert(0, '0')
  a7 = int(a7)

  a8 = b8.get()

  if a8 == '' or a8 == '-':
    a8 = '0'
    b8.delete(0, tk.END)
    b8.insert(0, '0')
  a8 = int(a8)

  a9 = b9.get()

  if a9 == '' or a9 == '-':
    a9 = '0'
    b9.delete(0, tk.END)
    b9.insert(0, '0')
  a9 = int(a9)

  a10 = b10.get()

  if a10 == '' or a10 == '-':
    a10 = '0'
    b10.delete(0, tk.END)
    b10.insert(0, '0')
  a10 = int(a10)

  a11 = b11.get()

  if a11 == '' or a11 == '-':
    a11 = '0'
    b11.delete(0, tk.END)
    b11.insert(0, '0')

  a11 = int(a11)

  a12 = b12.get()

  if a12 == '' or a12 == '-':
    a12 = '0'
    b12.delete(0, tk.END)
    b12.insert(0, '0')
  a12 = int(a12)

  a13 = b13.get()

  if a13 == '' or a13 == '-':
    a13 = '0'
    b13.delete(0, tk.END)
    b13.insert(0, '0')
  a13 = int(a13)

  a14 = b14.get()

  if a14 == '' or a14 == '-':
    a14 = '0'
    b14.delete(0, tk.END)
    b14.insert(0, '0')
  a14 = int(a14)

  a15 = b15.get()

  if a15 == '' or a15 == '-':
    a15 = '0'
    b15.delete(0, tk.END)
    b15.insert(0, '0')
  a15 = int(a15)

  a16 = b16.get()

  if a16 == '' or a16 == '-':
    a16 = '0'
    b16.delete(0, tk.END)
    b16.insert(0, '0')
  a16 = int(a16)

  a17 = b17.get()

  if a17 == '' or a17 == '-':
    a17 = '0'
    b17.delete(0, tk.END)
    b17.insert(0, '0')
  a17 = int(a17)

  a18 = b18.get()

  if a18 == '' or a18 == '-':
    a18 = '0'
    b18.delete(0, tk.END)
    b18.insert(0, '0')
  a18 = int(a18)

  a19 = b19.get()

  if a19 == '' or a19 == '-':
    a19 = '0'
    b19.delete(0, tk.END)
    b19.insert(0, '0')
  a19 = int(a19)

  a20 = b20.get()

  if a20 == '' or a20 == '-':
    a20 = '0'
    b20.delete(0, tk.END)
    b20.insert(0, '0')
  a20 = int(a20)

  a21 = b21.get()

  if a21 == '' or a21 == '-':
    a21 = '0'
    b21.delete(0, tk.END)
    b21.insert(0, '0')
  a21 = int(a21)

  a22 = b22.get()

  if a22 == '' or a22 == '-':
    a22 = '0'
    b22.delete(0, tk.END)
    b22.insert(0, '0')
  a22 = int(a22)

  a23 = b23.get()

  if a23 == '' or a23 == '-':
    a23 = '0'
    b23.delete(0, tk.END)
    b23.insert(0, '0')
  a23 = int(a23)

  a24 = b24.get()

  if a24 == '' or a24 == '-':
    a24 = '0'
    b24.delete(0, tk.END)
    b24.insert(0, '0')
  a24 = int(a24)

  a25 = b25.get()

  if a25 == '' or a25 == '-':
    a25 = '0'
    b25.delete(0, tk.END)
    b25.insert(0, '0')
  a25 = int(a25)

  A = np.matrix([[a1, a2, a3, a4, a5], [a6, a7, a8, a9, a10],
                 [a11, a12, a13, a14, a15], [a16, a17, a18, a19, a20],
                 [a21, a22, a23, a24, a25]])
  V = round(np.linalg.det(A))
  e_xx = tk.Entry(opred_5,
                  font=('Times', 15),
                  width=40,
                  justify=tk.CENTER,
                  bd=0,
                  highlightthickness=0)
  e_xx['state'] = tk.DISABLED
  e_xx.grid(row=6, column=0, columnspan=6, pady=3)
  e_xx['state'] = tk.NORMAL
  e_xx.delete(0, tk.END)
  e_xx.insert(0, V)
  e_xx['state'] = tk.DISABLED


def vvod_kv_ur(e1, e4, e7, koef):
  '''
    решение квадратных уравнений
    :param e1: коэф при x^2
    :param e4: коэф при x
    :param e7: свободный член
    :param koef:
    :return: ответ на квадратное кравнение
    '''
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
  if (b**2 - 4 * a * c) < 0:
    e_01 = tk.Entry(koef,
                    font=('Times', 15),
                    width=20,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_01['state'] = tk.DISABLED
    e_01.config(background='#000000', disabledbackground='#09bd87')
    e_01.grid(row=3, column=1, columnspan=5, pady=3)
    e_0 = tk.Entry(koef,
                   font=('Times', 15),
                   width=10,
                   justify=tk.CENTER,
                   bd=0,
                   highlightthickness=0)
    e_0.delete(0, tk.END)
    e_0.insert(0, 'Нет корней')
    e_0['state'] = tk.DISABLED
    e_0.config(background='#000000', disabledbackground='#f8ffff')
    e_0.grid(row=3, column=1, columnspan=5, pady=5)
    e_00 = tk.Entry(koef,
                    font=('Times', 15),
                    width=20,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_00['state'] = tk.DISABLED
    e_00.config(background='#000000', disabledbackground='#09bd87')
    e_00.grid(row=4, column=1, columnspan=5, pady=3)
  elif (b**2 - 4 * a * c) == 0:
    x = (-b) / 2 * a
    e_x = tk.Entry(koef,
                   font=('Times', 15),
                   width=10,
                   justify=tk.LEFT,
                   bd=0,
                   highlightthickness=0)
    e_x.insert(0, 'x    = ')
    e_x['state'] = tk.DISABLED
    e_x.config(background='#000000', disabledbackground='#f8ffff')
    e_x.grid(row=3, column=1, columnspan=5, pady=3)
    e_xx = tk.Entry(koef,
                    font=('Times', 15),
                    width=6,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_xx['state'] = tk.DISABLED
    e_xx.config(background='#000000', disabledbackground='#f8ffff')
    e_xx.grid(row=3, column=2, columnspan=6, pady=3)
    e_xx['state'] = tk.NORMAL
    e_xx.delete(0, tk.END)
    e_xx.insert(0, x)
    e_xx['state'] = tk.DISABLED
    e_00 = tk.Entry(koef,
                    font=('Times', 15),
                    width=20,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_00['state'] = tk.DISABLED
    e_00.config(background='#000000', disabledbackground='#09bd87')
    e_00.grid(row=4, column=1, columnspan=5, pady=3)
  else:
    d = b**2 - 4 * a * c
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    e_x1 = tk.Entry(koef,
                    font=('Times', 15),
                    width=10,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_x1.insert(0, 'x1   = ')
    e_x1['state'] = tk.DISABLED
    e_x1.config(background='#000000', disabledbackground='#f8ffff')
    e_x1.grid(row=3, column=1, columnspan=5, pady=3)
    e_01 = tk.Entry(koef,
                    font=('Times', 15),
                    width=6,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_01.config(background='#000000', disabledbackground='#f8ffff')
    e_01.grid(row=3, column=2, columnspan=6, pady=3)
    e_x2 = tk.Entry(koef,
                    font=('Times', 15),
                    width=10,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_x2.insert(0, 'x2   = ')
    e_x2['state'] = tk.DISABLED
    e_x2.config(background='#000000', disabledbackground='#f8ffff')
    e_x2.grid(row=4, column=1, columnspan=5, pady=3)
    e_02 = tk.Entry(koef,
                    font=('Times', 15),
                    width=6,
                    justify=tk.LEFT,
                    bd=0,
                    highlightthickness=0)
    e_02.config(background='#000000', disabledbackground='#f8ffff')
    e_02.grid(row=4, column=2, columnspan=6, pady=3)
    e_01.delete(0, tk.END)
    e_01.insert(0, x1)
    e_01['state'] = tk.DISABLED
    e_02.delete(0, tk.END)
    e_02.insert(0, x2)
    e_02['state'] = tk.DISABLED


def okno_kv_ur(t):
  '''
    решение квадратных уравнений
    :param e1: коэф при x^2
    :param e4: коэф при x
    :param e7: свободный член
    :param koef:
    :return: окно решения квадратного кравнения
    '''
  koef = tk.Toplevel(t)
  koef.minsize(width=320, height=500)
  koef['bg'] = '#09bd87'
  koef.grid()
  koef.title('Квадратное уравнение')

  ecmd = (koef.register(validate_e), '%P')
  e0 = tk.Entry(koef, font=('Times', 15), width=20, justify=tk.CENTER, bd=3)
  e0.insert(0, 'Введите коэффиценты')
  e0['state'] = tk.DISABLED
  e0.config(background='#000000', disabledbackground='#f8ffff')
  e0.grid(row=0, column=0, sticky='we', columnspan=7)
  e1 = tk.Entry(koef,
                font=('Times', 15),
                bg='#d3e1e8',
                bd=0,
                highlightthickness=0,
                width=5,
                justify=tk.CENTER,
                validate='key',
                validatecommand=ecmd)
  e1.focus()
  e1.grid(row=1, column=0, pady=3, sticky='wens')
  e2 = tk.Entry(koef,
                font=('Times', 15),
                bd=0,
                highlightthickness=0,
                width=5,
                justify=tk.CENTER)
  e2.insert(0, 'x²')
  e2['state'] = tk.DISABLED
  e2.config(background='#000000', disabledbackground='#f8ffff')
  e2.grid(row=1, column=1, pady=3, sticky='wens')
  e3 = tk.Entry(koef,
                font=('Times', 15),
                width=5,
                justify=tk.CENTER,
                bd=0,
                highlightthickness=0)
  e3.insert(0, '+')
  e3['state'] = tk.DISABLED
  e3.config(background='#000000', disabledbackground='#f8ffff')
  e3.grid(row=1, column=2, pady=3, sticky='wens')
  e4 = tk.Entry(koef,
                font=('Times', 15),
                bg='#d3e1e8',
                bd=0,
                highlightthickness=0,
                width=5,
                justify=tk.CENTER,
                validate='key',
                validatecommand=ecmd)
  e4.focus()
  e4.grid(row=1, column=3, pady=3, sticky='wens')
  e5 = tk.Entry(koef,
                font=('Times', 15),
                bd=0,
                highlightthickness=0,
                width=5,
                justify=tk.CENTER)
  e5.insert(0, 'x')
  e5['state'] = tk.DISABLED
  e5.config(background='#000000', disabledbackground='#f8ffff')
  e5.grid(row=1, column=4, pady=3, sticky='wens')
  e6 = tk.Entry(koef,
                font=('Times', 15),
                width=5,
                justify=tk.CENTER,
                bd=0,
                highlightthickness=0)
  e6.insert(0, '+')
  e6['state'] = tk.DISABLED
  e6.config(background='#000000', disabledbackground='#f8ffff')
  e6.grid(row=1, column=5, pady=3, sticky='wens')
  e7 = tk.Entry(koef,
                font=('Times', 15),
                bg='#d3e1e8',
                bd=0,
                highlightthickness=0,
                width=5,
                justify=tk.CENTER,
                validate='key',
                validatecommand=ecmd)
  e7.focus()
  e7.grid(row=1, column=6, pady=3, sticky='wens')
  tk.Button(koef,
            text='OK',
            bd=3,
            bg='#f0ffff',
            font=('Arial', 13),
            command=lambda: vvod_kv_ur(e1, e4, e7, koef)).grid(row=2,
                                                               column=0,
                                                               sticky='wens',
                                                               padx=2,
                                                               pady=2,
                                                               columnspan=7)
  koef.mainloop()


def press_key(event):
  '''
    организация ввода через клавиатуру
    :param event: событие на клавиатуре
    :return: реакция на данное событие
    '''
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
calc_etry = tk.Entry(calc,
                     justify=tk.RIGHT,
                     font=('Arial', 20),
                     width=20,
                     bd=5)
calc_etry.insert(0, '0')
calc_etry['state'] = tk.DISABLED
calc_etry.config(background='#000000', disabledbackground='#f8ffff')
calc_etry.grid(row=0, column=0, columnspan=4, sticky='we')
# Кнопки
but1 = [
  "M", "CE", "C", "⌫", "⅟х", "x²", "√х", "÷", "7", "8", "9", "×", "4", "5",
  "6", "-", "1", "2", "3", "+", "0", ".", "="
]
calc.bind('<Key>', press_key)
# Переменные
r, c = 1, 0
HZ = 0

for i in but1:
  if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: add_digit(v)).grid(row=r,
                                                     column=c,
                                                     sticky='wens',
                                                     padx=2,
                                                     pady=2)
  elif i in ['+', '-', '×', '÷', '.']:
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: add_sign(v)).grid(row=r,
                                                    column=c,
                                                    sticky='wens',
                                                    padx=2,
                                                    pady=2)
  elif i == '=':
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: equally(v)).grid(row=r,
                                                   column=c,
                                                   sticky='wens',
                                                   padx=2,
                                                   pady=2,
                                                   columnspan=2)
  elif i == '⅟х':
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: denominator(v)).grid(row=r,
                                                       column=c,
                                                       sticky='wens',
                                                       padx=2,
                                                       pady=2)
  elif i == 'x²':
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: sq(v)).grid(row=r,
                                              column=c,
                                              sticky='wens',
                                              padx=2,
                                              pady=2)
  elif i == '√х':
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: sq_r(v)).grid(row=r,
                                                column=c,
                                                sticky='wens',
                                                padx=2,
                                                pady=2)
  elif i == 'C':
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: Delete_0(v)).grid(row=r,
                                                    column=c,
                                                    sticky='wens',
                                                    padx=2,
                                                    pady=2)
  elif i == '⌫':
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: Delete_1(v)).grid(row=r,
                                                    column=c,
                                                    sticky='wens',
                                                    padx=2,
                                                    pady=2)
  elif i == 'CE':
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda v=i: Delete_2(v)).grid(row=r,
                                                    column=c,
                                                    sticky='wens',
                                                    padx=2,
                                                    pady=2)
  elif i == 'M':
    tk.Button(calc,
              text=i,
              bd=5,
              bg='#f0ffff',
              font=('Arial', 13),
              command=lambda: menu(calc)).grid(row=r,
                                               column=c,
                                               sticky='wens',
                                               padx=2,
                                               pady=2)
  calc.grid_rowconfigure(r, minsize=75)
  calc.grid_columnconfigure(c, minsize=70)
  c += 1
  if c > 3:
    c = 0
    r += 1

calc.mainloop()
