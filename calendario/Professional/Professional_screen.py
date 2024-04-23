import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#Professional registration interface
class ProfessionalScreen(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.conn = sqlite3.connect("database/usuarios.db")
        self.cursor = self.conn.cursor()
 
        self.entry_name_pro = tk.Entry(self)
        self.entry_phone_pro = tk.Entry(self)

        tk.Label(self, text="Name:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(self, text="Phone:").grid(row=1, column=0, sticky=tk.W)

        self.entry_name_pro.grid(row=0, column=1)
        self.entry_phone_pro.grid(row=1, column=1)
        
        self.pro_treeview = ttk.Treeview(
        self, columns=("Name_pro", "Phone_pro"), show="headings"
        )
        self.pro_treeview.heading("Name_pro", text="Name")
        self.pro_treeview.heading("Phone_pro", text="Phone")
        self.pro_treeview.grid(row=4, column=0, columnspan=3, pady=10, sticky="nsew")

        self.grid_rowconfigure(4, weight=1)
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)

        tk.Button(self, text="Show Info", command=self.show_info_pro).grid(
            row=3, column=2, pady=10)

        
        tk.Button(self, text="Register Professional", command=self.register_pro).grid(row=2, column=0, columnspan=2, pady=10)

    def add_pro(self, name_pro, phone_pro):
        
        conn = sqlite3.connect("database/usuarios.db")
        cursor = conn.cursor()

        cursor.execute('''
           INSERT OR FAIL INTO professional (name_pro, phone_pro)
           VALUES (?, ?)
        ''', (name_pro, phone_pro))

        conn.commit()
    
    def register_pro(self):
        name_pro = self.entry_name_pro.get()
        phone_pro = self.entry_phone_pro.get()

        if not name_pro or not phone_pro:
            messagebox.showerror("Error", "Please provide all the required information.")
        else:
            self.add_pro(name_pro, phone_pro)
            messagebox.showinfo("Registration", "Professional registered successfully!")
        self.entry_name_pro.delete(0, 'end')
        self.entry_phone_pro.delete(0, 'end')

    def show_info_pro(self):
        self.pro_treeview.delete(*self.pro_treeview.get_children())

        pro_data = self.cursor.execute(
            """
            SELECT professional.name_pro, professional.phone_pro
            FROM professional
        
        """
        ).fetchall()

        for professional in pro_data:
            name_pro, phone_pro = professional
            self.pro_treeview.insert("", "end", values=(name_pro, phone_pro))