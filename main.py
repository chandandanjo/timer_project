import tkinter
import time
from tkinter import Button, CENTER
from tkinter.ttk import Combobox
import threading


class MyWindow:
    def __init__(self, win):
        self.func_start = False
        self.ddl1_var = tkinter.IntVar()
        self.ddl1_options = [f'{i}' for i in range(1, 11)]
        self.ddl1 = Combobox(win, textvariable=self.ddl1_var, values=self.ddl1_options, state='readonly')
        self.ddl1.place(relx=0.7, rely=0.7, relheight=.1, relwidth=.2, anchor=CENTER)
        self.ddl1.bind('<<ComboboxSelected>>', self.set_timer)

        self.lbl1_var = tkinter.IntVar()
        self.lbl1 = tkinter.Label(win, textvariable=self.lbl1_var)
        self.lbl1.place(relx=0.5, rely=0.2, relheight=.4, relwidth=.8, anchor=CENTER)
        self.lbl1.config(font=("Courier", 30))

        self.b1 = Button(win, text="Start", command=self.threading1)
        self.b1.place(relx=0.2, rely=0.7, relheight=.1, relwidth=.2, anchor=CENTER)

        self.b2 = Button(win, text="Reset", command=self.reset)
        self.b2.place(relx=0.2, rely=0.5, relheight=.1, relwidth=.2, anchor=CENTER)

    def start(self):
        self.func_start = True
        while self.func_start:
            self.b1['state'] = tkinter.DISABLED
            init_val = int(self.ddl1.get())
            for i in range(init_val, -1, -1):
                if self.func_start:
                    self.lbl1_var.set(i)
                    window.update_idletasks()
                    time.sleep(1)
                else:
                    break
            if self.func_start:
                continue
            else:
                break
        self.b1['state'] = tkinter.NORMAL

    def threading1(self):
        time.sleep(1)
        t1 = threading.Thread(target=self.start)
        t1.start()

    def reset(self):
        if self.func_start:
            self.func_start = False
            self.lbl1_var.set(int(self.ddl1.get()))
            print(threading.active_count())
            # time.sleep(1)
            self.threading1()

    def set_timer(self, event):
        self.lbl1_var.set(int(self.ddl1.get()))


window = tkinter.Tk()
Screen = MyWindow(window)
window.title('Timer')
window.geometry("500x400+10+10")
window.mainloop()
