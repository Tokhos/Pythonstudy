import tkinter as tk


class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Main Screen")

        self.button1 = tk.Button(self, text="Open Screen 1", command=self.open_screen1)
        self.button1.pack(pady=20)

        self.button2 = tk.Button(self, text="Open Screen 2", command=self.open_screen2)
        self.button2.pack(pady=20)

        self.screen3_button = tk.Button(self, text="Open Screen 3", command=self.open_screen3)
        self.screen3_button.pack(pady=20)

    def open_screen1(self):
        screen1 = Screen1(self)

    def open_screen2(self):
        screen2 = Screen2(self)

    def open_screen3(self):
        screen3 = Screen3(self)


class Screen1(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Screen 1")

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Submit", command=self.submit)
        self.button.pack(pady=10)

    def submit(self):
        entry_value = self.entry.get()
        print("Screen 1 Entry:", entry_value)


class Screen2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Screen 2")

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        self.button = tk.Button(self, text="Submit", command=self.submit)
        self.button.pack(pady=10)

    def submit(self):
        entry_value = self.entry.get()
        print("Screen 2 Entry:", entry_value)


class Screen3(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Screen 3")

        self.screen4_button = tk.Button(self, text="Open Screen 4", command=self.open_screen4)
        self.screen4_button.pack(pady=20)

    def open_screen4(self):
        screen4 = Screen4(self)


class Screen4(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Screen 4")

        self.label = tk.Label(self, text="This is Screen 4")
        self.label.pack(pady=10)


if __name__ == "__main__":
    app = MainScreen()
    app.mainloop()

