import tkinter as tk
from tkinter import messagebox
import sqlite3

class ProfessionalScreen(tk.Frame):
    def __init__(self, parent, update_combobox_pro):
        super().__init__(parent)

        self.update_combobox_pro = update_combobox_pro

        
        self.entry_name_pro = tk.Entry(self)
        self.entry_phone_pro = tk.Entry(self)

        
        tk.Label(self, text="Name:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self, text="Phone:").grid(row=1, column=0, sticky=tk.W)

        
        self.entry_name_pro.grid(row=0, column=1)
        self.entry_phone_pro.grid(row=1, column=1)

        
        tk.Button(self, text="Register Professional", command=self.register_pro).grid(row=2, column=0, columnspan=2, pady=10)

    def add_pro(self, name_pro, phone_pro):
        
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        cursor.execute('''
            INSERT OR FAIL INTO professional (name_pro, phone_pro)
            VALUES (?, ?)
        ''', (name_pro, phone_pro))

        conn.commit()
        self.update_combobox_pro()

    def register_pro(self):
        name_pro = self.entry_name_pro.get()
        phone_pro = self.entry_phone_pro.get()

        if not name_pro or not phone_pro:
            messagebox.showerror("Error", "Please provide all the required information.")
        else:
            self.add_pro(name_pro, phone_pro)
            messagebox.showinfo("Registration", "Professional registered successfully!")
