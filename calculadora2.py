import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_button(1)
        self.create_button(2)
        self.create_button(3)
        self.create_button(4)
        self.create_button(5)
        self.create_button(6)
        self.create_button(7)
        self.create_button(8)
        self.create_button(9)
        self.create_button(0)

        self.create_button('+')
        self.create_button('-')
        self.create_button('*')
        self.create_button('/')
        self.create_button('.')

        self.create_clear_button()
        self.create_equal_button()

    def create_button(self, number):
        tk.Button(self.master, text=number, padx=40, pady=20, command=lambda: self.button_click(number)).grid(row=self.get_button_row(number), column=self.get_button_column(number))

    def create_clear_button(self):
        tk.Button(self.master, text='Limpar', padx=79, pady=20, command=self.clear).grid(row=1, column=0, columnspan=2)

    def create_equal_button(self):
        tk.Button(self.master, text='=', padx=91, pady=20, command=self.calculate).grid(row=1, column=2, columnspan=2)

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(current) + str(number))

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        expression = self.entry.get()
        try:
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Erro")

    def get_button_row(self, number):
        if number in [1, 2, 3]:
            return 4
        elif number in [4, 5, 6]:
            return 3
        elif number in [7, 8, 9]:
            return 2
        else:
            return 1

    def get_button_column(self, number):
        if number in [1, 4, 7]:
            return 0
        elif number in [2, 5, 8, 0]:
            return 1
        elif number in [3, 6, 9]:
            return 2
        else:
            return 3

root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
