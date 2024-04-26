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

    while pause:
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

        time.sleep(0.0001)
        hours_label.config(text=f"{hours}")
        minutes_label.config(text=f"{minutes}")
        seconds_label.config(text=f"{seconds}")


def start_new_thread():
    Thread(target=start_timer).start()


root = Tk()

frm = ttk.Frame(root, padding=80)
root.title("Timer с интерфейсом на Python")
root.geometry("640x480")
frm.grid()

hours_label = ttk.Label(frm, text="00")
hours_label.grid(column=1, row=0)

ttk.Label(frm, text=" :").grid(column=2, row=0)

minutes_label = ttk.Label(frm, text=" 00")
minutes_label.grid(column=3, row=0)

ttk.Label(frm, text=" :").grid(column=4, row=0)

seconds_label = ttk.Label(frm, text="00")
seconds_label.grid(column=5, row=0)

Button(text="stop",
       background="#555",
       foreground="#FF0000",
       padx="8",
       pady="4",
       font="6",
       command=stop_timer
       ).grid(column=0, row=1)


Button(text="reset",
       background="#FF0000",
       foreground="#ccc",
       padx="8",
       pady="4",
       font="6",
       command=reset_timer
       ).grid(column=1, row=1)


Button(text="start",
       background="#007FFF",
       foreground="#ccc",
       padx="8",
       pady="4",
       font="6",
       command=start_new_thread
       ).grid(column=2, row=1)

root.mainloop()
