import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class EditScheduleScreen(tk.Toplevel):
    def __init__(self, master, schedule_data):
        super().__init__(master)

        self.title("Edit Schedule")
        self.conn = sqlite3.connect("database/usuarios.db")
        self.cursor = self.conn.cursor()

        self.schedule_data = schedule_data  # Schedule data to be edited


        # Create labels and entry fields for editing schedule information
        self.user_label = tk.Label(self, text="User:")
        self.user_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.user_entry = tk.Entry(self)
        self.user_entry.insert(0, schedule_data[0])  # Set initial value to the current user
        self.user_entry.grid(row=0, column=1, padx=5, pady=5)

        self.professional_label = tk.Label(self, text="Professional:")
        self.professional_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.professional_entry = tk.Entry(self)
        self.professional_entry.insert(0, schedule_data[1])  # Set initial value to the current professional
        self.professional_entry.grid(row=1, column=1, padx=5, pady=5)

        self.date_label = tk.Label(self, text="Date:")
        self.date_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.date_entry = tk.Entry(self)
        self.date_entry.insert(0, schedule_data[2])  # Set initial value to the current date
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)



        # Buttons for saving or canceling the changes
        self.save_button = tk.Button(self, text="Save", command=self.save_schedule_changes)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        self.cancel_button = tk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    def save_schedule_changes(self):
        # Get edited values from entry fields
        new_id_user = self.user_entry.get()
        new_id_pro = self.professional_entry.get()
        new_available_data = self.date_entry.get()


        # Lookup IDs based on names
        user_id = self.get_user_id(new_id_user)
        professional_id = self.get_professional_id(new_id_pro)

        if user_id is None or professional_id is None:
            messagebox.showerror("Error", "User or professional not found.")
            return

        # Display a confirmation messagebox
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to save changes?")

        if confirmation:
            # Update the schedule data
            self.schedule_data[0] = new_id_user
            self.schedule_data[1] = new_id_pro
            self.schedule_data[2] = new_available_data


            # Update the database with the new data
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE schedule
                SET id_user = ?, id_pro = ?, available_data = ?
                WHERE id_user = ? AND id_pro = ? AND available_data = ?
            """, (new_id_user, new_id_pro, new_available_data, self.schedule_data[0], self.schedule_data[1], self.schedule_data[2]))
            self.conn.commit()

            # Close the EditScheduleScreen
            self.destroy()

            # Display a warning messagebox
            messagebox.showwarning("Success", "Changes saved successfully!")

    def get_user_id(self, user_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM users WHERE name = ?", (user_name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def get_professional_id(self, professional_name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_pro FROM professional WHERE name_pro = ?", (professional_name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None