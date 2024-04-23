import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

######
class EditScheduleScreen(tk.Toplevel):
    def __init__(self, master, id_schedule):
        super().__init__(master)

        self.title("Edit User")
        self.conn = sqlite3.connect("database/usuarios.db")
        self.cursor = self.conn.cursor()
        self.id_schedule = id_schedule

        # Consulta para obter informações do id_schedule
        self.cursor.execute("SELECT available_data FROM schedule WHERE id_schedule = ?", (id_schedule,))
        schedule_data = self.cursor.fetchone()
        if schedule_data:
            self.current_date = schedule_data[0]
        else:
            self.current_date = ""  # Define como vazio se não encontrar dados
        
        self.date_label = tk.Label(self, text="Current Date:")
        self.date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.current_date_label = tk.Label(self, text=self.current_date)
        self.current_date_label.grid(row=0, column=1, padx=5, pady=5)

        self.new_date_label = tk.Label(self, text="New Date:")
        self.new_date_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_changes)
        self.save_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    def save_changes(self):
        new_date = self.date_entry.get()

        # Update the Treeview with the new data
        self.cursor.execute("""
            UPDATE schedule
            SET available_data = ?
            WHERE id_schedule = ?
        """, (new_date, self.id_schedule))
        self.conn.commit()
        
        messagebox.showwarning("Sucess", "Deu bom")
       
        print("New Date:", new_date)
        print("ID Schedule:", self.id_schedule)
        
        self.destroy()