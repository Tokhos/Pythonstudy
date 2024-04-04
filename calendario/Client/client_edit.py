import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class EditUserScreen(tk.Toplevel):
    def __init__(self, master, user_data):
        super().__init__(master)

        self.title("Edit User")
        self.conn = sqlite3.connect("database/usuarios.db")
        self.cursor = self.conn.cursor()

        self.user_data = user_data  # User data to be edited

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = tk.Entry(self)
        self.name_entry.insert(0, user_data[0])  # Set initial value to the current name
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self)
        self.phone_entry.insert(0, user_data[1])  # Set initial value to the current phone
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.email_entry = tk.Entry(self)
        self.email_entry.insert(0, user_data[2])  # Set initial value to the current email
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(self, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.address_entry = tk.Entry(self)
        self.address_entry.insert(0, user_data[3])  # Set initial value to the current address
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_changes)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def save_changes(self):
        
        
        
        new_name = self.name_entry.get()
        new_phone = self.phone_entry.get()
        new_email = self.email_entry.get()
        new_address = self.address_entry.get()
       
       
        self.user_data[0] = new_name
        self.user_data[1] = new_phone
        self.user_data[2] = new_email
        self.user_data[3] = new_address
        
        # Update the Treeview with the new data

        self.cursor.execute("""
            UPDATE users
            SET name = ?, phone = ?, mail = ?, adress = ?
            WHERE name = ?
        """, (new_name, new_phone, new_email, new_address, self.user_data[0]))
        self.conn.commit()
       
        
        self.destroy()