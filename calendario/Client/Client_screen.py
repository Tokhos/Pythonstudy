import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class ClientScreen(tk.Frame):
    def __init__(self, parent, update_combobox_users):
        super().__init__(parent)

        self.update_combobox_users = update_combobox_users

        
        self.entry_name = tk.Entry(self)
        self.entry_phone = tk.Entry(self)
        self.entry_mail = tk.Entry(self)
        self.entry_adress = tk.Entry(self)

        
        tk.Label(self, text="Name:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self, text="Phone:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(self, text="Mail:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(self, text="Adress:").grid(row=3, column=0, sticky=tk.W)

        
        self.entry_name.grid(row=0, column=1)
        self.entry_phone.grid(row=1, column=1)
        self.entry_mail.grid(row=2, column=1)
        self.entry_adress.grid(row=3, column=1)

        
        tk.Button(self, text="Register User", command=self.register_user).grid(row=4, column=0, columnspan=2, pady=10)

    def add_user(self, name, phone, mail, adress, status):
        
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()

        register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT OR FAIL INTO users (name, phone, mail, adress, register_date, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, phone, mail, adress, register_date, status))

        conn.commit()
        self.update_combobox_users()

    def register_user(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        mail = self.entry_mail.get()
        adress = self.entry_adress.get()
        status = 1

        if not name or not mail or not adress or not phone:
            messagebox.showerror("Error", "Please provide all the required information.")
        else:
            self.add_user(name, phone, mail, adress, status)
            messagebox.showinfo("Registration", "User registered successfully!")
