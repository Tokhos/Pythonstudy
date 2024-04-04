import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

class EditScheduleScreen(tk.Toplevel):
    def __init__(self, master, schedule_id, id_user, id_pro):
        super().__init__(master)
        self.title("Edit Schedule")

        self.conn = sqlite3.connect("database/usuarios.db")
        self.cursor = self.conn.cursor()

        self.schedule_id = schedule_id
        self.id_user = id_user
        self.id_pro = id_pro

        self.date_label = tk.Label(self, text="New Date:")
        self.date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_changes)
        self.save_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

    def save_changes(self):
        new_date = self.date_entry.get()

        if new_date:
            try:
                # Update the date in the database
                self.cursor.execute("""
                    UPDATE schedule
                    SET available_data = ?
                    WHERE id_user = ? AND id_pro = ?
                """, (new_date, self.id_user, self.id_pro))
                self.conn.commit()

                messagebox.showinfo("Success", "Date updated successfully.")
                self.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Database error: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter a new date.")