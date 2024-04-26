# импорт библиотеки с интерфейсом (окнами)
# tkinter, pyqt5, pyside6

# импорт всей библиотеки контрал клик (отображение всех методов,исходные коды)
# import time

# использование одного из методов библиотеки
# time.sleep(1)

# импортируем библиотеку для работы с окнами(интерфейсом) импорт всей библиотеки
# импорт всех функций, классов и переменных (может вызвать коллизию имен)
# from tkinter import *

# импорт всей библиотеки с присвоением псевдонима
# import tkinter as tk

# импорт отдельной функции из модуля (уже написанного файла)
# from. calc import calc_3

# pip install pyinstaller
# pyinstaller --onefile hello.py


# from tkinter import ttk
import time
from tkinter import *
from tkinter import ttk
from threading import Thread

hours = 0
minutes = 0
seconds = 0

pause = True


def stop_timer():
    global pause
    pause = False


def reset_timer():
    global hours
    hours = 0
    global minutes
    minutes = 0
    global seconds
    seconds = 0
    hours_label.config(text=f"{hours}")
    minutes_label.config(text=f"{minutes}")
    seconds_label.config(text=f"{seconds}")


def start_timer():
    global pause
    pause = True

    global hours
    global minutes
    global seconds

    # hours = 0
    # minutes = 0
    # seconds = 0

    while pause:
        # while minutes < 5:
        #     break
        # seconds = seconds + 1
        seconds += 1
        if seconds > 59:
            minutes += 1
            seconds = 0

        if minutes > 59:
            hours += 1
            minutes = 0

        if hours > 23:
            minutes = 0
            seconds = 0
            hours = 0

        # if minutes > 5:
        #     break

        time.sleep(0.0001)
        hours_label.config(text=f"{hours}")
        minutes_label.config(text=f"{minutes}")
        seconds_label.config(text=f"{seconds}")

        # print(f"{hours}:{minutes}:{seconds}")


# определение (создание) функции
def start_new_thread():
    # for i in range(0, 100): # можно запустить множество(100 в данном случае) потоков
    Thread(target=start_timer).start()


# вызов функции
# start_new_thread()

# Инициализация инстанса т.е. создание объекта tkinter
root = Tk()

frm = ttk.Frame(root, padding=80)
root.title("Timer с интерфейсом на Python")
root.geometry("640x480")
frm.grid()

# часы
hours_label = ttk.Label(frm, text="00")
hours_label.grid(column=1, row=0)

ttk.Label(frm, text=" :").grid(column=2, row=0)

# минуты
minutes_label = ttk.Label(frm, text=" 00")
minutes_label.grid(column=3, row=0)

ttk.Label(frm, text=" :").grid(column=4, row=0)

# секунды
seconds_label = ttk.Label(frm, text="00")
seconds_label.grid(column=5, row=0)

# кнопка стоп
Button(text="stop",
       background="#555",
       foreground="#FF0000",
       padx="8",
       pady="4",
       font="6",
       command=stop_timer
       ).grid(column=0, row=1)

# кнопка сброс
Button(text="reset",
       background="#FF0000",
       foreground="#ccc",
       padx="8",
       pady="4",
       font="6",
       command=reset_timer
       ).grid(column=1, row=1)

# кнопка старт
Button(text="start",
       background="#007FFF",
       foreground="#ccc",
       padx="8",
       pady="4",
       font="6",
       command=start_new_thread  # ссылка на запуск функции
       ).grid(column=2, row=1)

root.mainloop()
