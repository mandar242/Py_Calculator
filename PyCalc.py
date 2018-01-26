from tkinter import *
from tkinter import ttk


class Calculator:
    calc_value = 0.0

    sub_trigger = False
    add_trigger = False
    div_trigger = False
    multi_trigger = False

    def __init__(self, root):

        self.entry_value = StringVar(root, value="")

        root.title("Calculator")

        root.geometry("600x600")

        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=10)
        style.configure("TEntry", font="Serif 18", padding=10)

        self.number_entry = ttk.Entry(root, textvariable=self.entry_value,
                                      width=50)

        self.number_entry.grid(row=0, columnspan=4)

        #First Row of buttons

        self.button7 = ttk.Button(root, text="7",
                                  command=lambda: self.button_press('7')
                                  ).grid(row=1, column=0)

        self.button8 = ttk.Button(root, text="8",
                                  command=lambda: self.button_press('8')
                                  ).grid(row=1, column=1)

        self.button9 = ttk.Button(root, text="9",
                                  command=lambda: self.button_press('9')
                                  ).grid(row=1, column=2)

        self.button_division = ttk.Button(root, text="/",
                                          command=lambda: self.math_button_press('/')
                                          ).grid(row=1, column=3)


root = Tk()

calc = Calculator(root)

root.mainloop()
