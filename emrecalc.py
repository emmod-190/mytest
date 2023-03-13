import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("emrecalc")
        master.configure(bg="#191919")

        self.entry = tk.Entry(master, width=25, bg="#252525", fg="#FFFFFF")
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("+", 1, 3, "#C1BA47")
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3, "#C25448")
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("C", 3, 3, "#534746")
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2, "#24752E")
        self.create_button("/", 4, 3, "#553F5F")

    def create_button(self, text, row, col, color="#252525"):
        button = tk.Button(self.master, text=text, width=5, height=2, bg=color,
                           fg="#FFFFFF", command=lambda: self.button_click(text))
        button.grid(row=row, column=col, padx=2, pady=2)

    def button_click(self, text):
        if text == "C":
            self.entry.delete(0, tk.END)
        elif text == "=":
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        else:
            self.entry.insert(tk.END, text)


root = tk.Tk()
app = Calculator(root)
root.mainloop()
