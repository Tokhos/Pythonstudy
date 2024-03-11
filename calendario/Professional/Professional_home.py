import tkinter as tk
from tkinter import ttk


class Prohome(tk.Frame):
    def __init__(self, parent, update_combobox_users):
        super().__init__(parent)
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill=tk.BOTH)
        
        self.update_combobox_users = update_combobox_users

        self.button1 = tk.Button(self, text="Professional List", width=20, height=5, command=lambda: self.notebook.select(3))
        self.button1.pack(pady=20)

        self.button2 = tk.Button(self, text="Professional Select", width=20, height=5, command=lambda: self.notebook.select(4))
        self.button2.pack(pady=20)
        